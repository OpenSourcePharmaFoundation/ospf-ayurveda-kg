#!/usr/bin/env bash
# Run a sequence of prompts as chained Claude Code background agents.
#
# Usage:
#   ./ospf chain [chain-file.md] [options]
#
# Each step is launched as a separate `claude --bg` job, and the next step
# starts only after the previous one completes. Run without a file argument
# in a terminal to pick from the chain files under docs/prompts/ (files named
# *-prompt.md). A bare name also works: `./ospf chain foo` looks for
# docs/prompts/foo-prompt.md, then docs/prompts/foo.md.
#
# Chain file format (Markdown):
#
#   # Chain Name
#
#   effort: low
#   permissions: auto
#
#   ## Step 1 Name
#
#   Prompt text for the first step goes here.
#   Can be multiple lines of markdown.
#
#   -----[NEXT_PROMPT]-----
#
#   ## Step 2 Name
#
#   model: haiku
#   effort: medium
#
#   Prompt text for the second step.
#
# Chain-level metadata (model, effort, permissions, cwd, category, preflight)
# goes between the H1 and the first H2. Per-step metadata goes right after the
# H2 heading. The delimiter -----[NEXT_PROMPT]----- separates steps. Any other
# `## heading` inside a step is treated as the step's name, not prompt text,
# so keep sub-structure inside a step to `###` or lower.
#
#   model        claude --model (e.g. sonnet, opus)
#   effort       claude --effort (low, medium, high)
#   permissions  claude --permission-mode (e.g. auto, acceptEdits, plan)
#   cwd          extra directory the agent may work in (claude --add-dir);
#                relative values are taken from the repo root
#   category     prefix for the agent name, shown in `claude agents`
#   preflight    checks to run before each step (see below)
#
# Every step's prompt body should begin with the standard chain-step preamble,
# copied verbatim from the marked block in docs/prompts/chain-step-preamble.md.
# Its closing `result:` line is what makes a step's completion detectable: see
# --settle-timeout below for why.
#
# Preflight checks (metadata key `preflight:`, chain-level or per-step;
# per-step overrides chain-level). Comma/space-separated tokens, verified
# before every step attempt; a failing check is re-polled until
# --preflight-timeout, then the chain aborts with a resume hint:
#   gh                    gh CLI is authenticated (gh auth status)
#   cmd=NAME              NAME is on PATH (e.g. cmd=glow, cmd=pandoc)
#   file=PATH             PATH exists (relative to the repo root)
#
# Per-step state is saved to tmp/chain-runs/ after every step, so a failed
# or interrupted chain can be resumed with --resume (completed steps are
# skipped). Failed steps are retried automatically (--retries, default 1).
#
# Options:
#   --start-from N    Start from step N (1-indexed), skipping earlier steps
#   --resume          Resume this chain from its saved state, skipping steps
#                     that already completed in a previous run
#   --fresh           Ignore saved state and start from step 1
#   --retries N       Relaunch a failed step up to N times (default: 1; 0 off)
#   --skip-preflight  Skip preflight checks declared in the chain file
#   --preflight-timeout S  Keep re-polling a failing preflight for up to S
#                     seconds before aborting the chain (default: 300)
#   --dry-run         Print what would run without launching agents
#   --poll-interval S Seconds between status checks (default: 10)
#   --blocked-timeout S  Fail a step whose agent sits blocked on a permission
#                     prompt for S seconds (default: 900; the agent is left
#                     running for manual triage via: claude agents)
#   --settle-timeout S  Treat a step as complete once its agent has been idle
#                     with nothing in flight for S seconds while still
#                     reporting "working" (default: 120). A background agent's
#                     final state is inferred from the wording of its last
#                     message; when that inference does not resolve, the job
#                     keeps reporting "working" forever. This is the backstop.
#   --stop-on-fail    Abort the chain if any step fails (default: continue)
#   --pick            Show the interactive file picker
#   -h, --help        Show this help

set -euo pipefail

# ─── Resolve paths ──────────────────────────────────────────────────────────

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SELF_DIR/.." && pwd)"
PROMPTS_DIR="$REPO_ROOT/docs/prompts"
# ./ospf cds to the repo root before running us; it records where the user
# actually was so relative file arguments still resolve.
CALLER_PWD="${OSPF_CALLER_PWD:-$PWD}"

# ─── Colors ─────────────────────────────────────────────────────────────────

if [[ -t 1 ]]; then
  BOLD=$'\033[1m' DIM=$'\033[2m' GREEN=$'\033[32m' YELLOW=$'\033[33m'
  CYAN=$'\033[36m' RED=$'\033[31m' RESET=$'\033[0m'
else
  BOLD='' DIM='' GREEN='' YELLOW='' CYAN='' RED='' RESET=''
fi

# ─── Args ───────────────────────────────────────────────────────────────────

POLL_INTERVAL=10
BLOCKED_TIMEOUT=900
SETTLE_TIMEOUT=120
START_FROM=1
DRY_RUN=false
STOP_ON_FAIL=false
PICK_MODE=false
CHAIN_FILE=""
RESUME=false
FRESH=false
RETRIES=1
SKIP_PREFLIGHT=false
PREFLIGHT_TIMEOUT=300

usage() {
  sed -nE '2,/^$/s/^# ?//p' "$0"
  exit "${1:-0}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --start-from)  START_FROM="$2"; shift 2 ;;
    --resume)      RESUME=true; shift ;;
    --fresh)       FRESH=true; shift ;;
    --retries)     RETRIES="$2"; shift 2 ;;
    --skip-preflight) SKIP_PREFLIGHT=true; shift ;;
    --preflight-timeout) PREFLIGHT_TIMEOUT="$2"; shift 2 ;;
    --dry-run)     DRY_RUN=true; shift ;;
    --poll-interval) POLL_INTERVAL="$2"; shift 2 ;;
    --blocked-timeout) BLOCKED_TIMEOUT="$2"; shift 2 ;;
    --settle-timeout) SETTLE_TIMEOUT="$2"; shift 2 ;;
    --stop-on-fail)  STOP_ON_FAIL=true; shift ;;
    --pick)        PICK_MODE=true; shift ;;
    -h|--help)     usage 0 ;;
    -*)            echo "Unknown option: $1" >&2; usage 1 ;;
    *)
      if [[ -z "$CHAIN_FILE" ]]; then
        CHAIN_FILE="$1"
      else
        echo "Unexpected argument: $1" >&2; usage 1
      fi
      shift ;;
  esac
done

# ─── Interactive picker ─────────────────────────────────────────────────────

pick_chain_file() {
  if [[ ! -d "$PROMPTS_DIR" ]]; then
    echo "No prompt chains found — $PROMPTS_DIR does not exist." >&2
    exit 1
  fi

  # Discover prompt files recursively
  local -a all_paths=() all_names=() all_dates=() all_titles=() all_steps=()
  while IFS= read -r -d '' fpath; do
    local fname
    fname=$(basename "$fpath")
    # Extract date (yyyy-mm-dd) from filename
    local fdate=""
    if [[ "$fname" =~ ([0-9]{4}-[0-9]{2}-[0-9]{2})-prompt\.md$ ]]; then
      fdate="${BASH_REMATCH[1]}"
    fi
    # Extract chain name from H1
    local title=""
    title=$(grep -m1 '^# ' "$fpath" 2>/dev/null | sed 's/^# //')
    title="${title:-$fname}"
    # Count steps (delimiters + 1)
    local delim_count
    delim_count=$(grep -c '^\-\-\-\-\-\[NEXT_PROMPT\]\-\-\-\-\-$' "$fpath" 2>/dev/null || echo 0)
    local nsteps=$((delim_count + 1))
    # Relative path from repo root
    local relpath="${fpath#"$REPO_ROOT"/}"

    all_paths+=("$fpath")
    all_names+=("$relpath")
    all_dates+=("$fdate")
    all_titles+=("$title")
    all_steps+=("$nsteps")
  done < <(find "$PROMPTS_DIR" -type f -name '*-prompt.md' -print0 2>/dev/null)

  local total=${#all_paths[@]}
  if [[ "$total" -eq 0 ]]; then
    echo "No prompt chain files (*-prompt.md) found in $PROMPTS_DIR" >&2
    exit 1
  fi

  # ── Sort indices ──
  local sort_mode="date"  # date | alpha
  local -a sorted_indices=()

  _sort_items() {
    sorted_indices=()
    local -a pairs=()
    local i
    if [[ "$sort_mode" == "date" ]]; then
      for (( i=0; i<total; i++ )); do
        pairs+=("${all_dates[$i]:-0000-00-00}|$i")
      done
      while IFS='|' read -r _ idx; do
        sorted_indices+=("$idx")
      done < <(printf '%s\n' "${pairs[@]}" | sort -t'|' -k1,1r)
    else
      for (( i=0; i<total; i++ )); do
        pairs+=("${all_names[$i]}|$i")
      done
      while IFS='|' read -r _ idx; do
        sorted_indices+=("$idx")
      done < <(printf '%s\n' "${pairs[@]}" | sort -t'|' -k1,1f)
    fi
  }

  _sort_items

  # ── Fuzzy search ──
  local search_query=""
  local -a vis_indices=()
  local vis_count=0
  local selected=0

  _fuzzy_match() {
    local query="${1,,}" target="${2,,}"
    local qi=0 qlen=${#query}
    for (( ti=0; ti<${#target} && qi<qlen; ti++ )); do
      [[ "${query:$qi:1}" == "${target:$ti:1}" ]] && ((++qi)) || true
    done
    (( qi == qlen ))
  }

  _apply_filter() {
    vis_indices=()
    local i ri
    for (( i=0; i<total; i++ )); do
      ri=${sorted_indices[$i]}
      if [[ -z "$search_query" ]] || _fuzzy_match "$search_query" "${all_names[$ri]} ${all_titles[$ri]}"; then
        vis_indices+=("$ri")
      fi
    done
    vis_count=${#vis_indices[@]}
    if (( selected >= vis_count )); then
      selected=$(( vis_count > 0 ? vis_count - 1 : 0 ))
    fi
  }

  _apply_filter

  _highlight() {
    local query="$1" text="$2"
    [[ -z "$query" ]] && { printf '%s' "$text"; return; }
    local lq="${query,,}" lt="${text,,}"
    local out="" qi=0 qlen=${#query}
    for (( ti=0; ti<${#text}; ti++ )); do
      if (( qi < qlen )) && [[ "${lt:$ti:1}" == "${lq:$qi:1}" ]]; then
        out+="${GREEN}${text:$ti:1}${RESET}"
        ((++qi))
      else
        out+="${text:$ti:1}"
      fi
    done
    printf '%s' "$out"
  }

  # ── TUI ──
  local term_lines=0

  _get_term_height() {
    term_lines=${LINES:-0}
    if (( term_lines <= 0 )); then
      local sz
      sz=$(stty size 2>/dev/null) || true
      [[ -n "$sz" ]] && term_lines=${sz%% *}
    fi
    (( term_lines <= 0 )) && term_lines=$(tput lines 2>/dev/null || echo 24)
  }

  local scroll_top=0

  _adjust_scroll() {
    _get_term_height
    local avail=$(( term_lines - 5 ))
    (( avail < 3 )) && avail=3
    (( vis_count == 0 )) && { scroll_top=0; return; }
    (( selected < 0 )) && selected=0
    (( selected >= vis_count )) && selected=$((vis_count - 1))
    (( selected < scroll_top )) && scroll_top=$selected
    while (( selected - scroll_top >= avail )); do
      scroll_top=$((scroll_top + 1))
    done
  }

  tput smcup 2>/dev/null || true
  tput civis 2>/dev/null || true
  trap '_picker_cleanup' EXIT INT
  trap '_draw_picker' WINCH

  _picker_cleanup() {
    trap '' WINCH
    tput cnorm 2>/dev/null || true
    tput rmcup 2>/dev/null || true
    stty sane 2>/dev/null || true
  }

  _draw_picker() {
    _adjust_scroll
    tput cup 0 0 2>/dev/null || printf "\033[H"
    printf "\033[J"
    echo ""

    # Header
    if [[ -n "$search_query" ]]; then
      printf "  ${BOLD}>${RESET} ${GREEN}%s${RESET}${DIM}|${RESET}" "$search_query"
      if (( vis_count == 0 )); then
        printf "  ${RED}no matches${RESET}"
      else
        printf "  ${DIM}%d of %d${RESET}" "$vis_count" "$total"
      fi
      printf "\n"
    else
      printf "  ${BOLD}Prompt Chains${RESET}  ${DIM}(%d files, sorted by %s)${RESET}\n" "$total" "$sort_mode"
    fi

    # Scroll-up indicator
    if (( scroll_top > 0 )); then
      printf "  ${DIM}▲ %d above${RESET}\n" "$scroll_top"
    else
      echo ""
    fi

    # Items
    if (( vis_count == 0 )); then
      printf "  ${DIM}No chains match your search${RESET}\n"
      echo ""
    else
      local avail=$(( term_lines - 5 ))
      (( avail < 3 )) && avail=3
      local rendered=0

      for (( vi=scroll_top; vi<vis_count && rendered<avail; vi++ )); do
        local ri=${vis_indices[$vi]}
        local title="${all_titles[$ri]}"
        local date="${all_dates[$ri]}"
        local steps="${all_steps[$ri]}"
        local name="${all_names[$ri]}"
        local date_display=""
        [[ -n "$date" ]] && date_display=" ${DIM}($date)${RESET}"
        local steps_display="${DIM}${steps} steps${RESET}"

        if (( vi == selected )); then
          if [[ -n "$search_query" ]]; then
            printf "  ${CYAN}${BOLD}▸${RESET} %s%s  %s\n" "$(_highlight "$search_query" "$title")" "$date_display" "$steps_display"
          else
            printf "  ${CYAN}${BOLD}▸ %s${RESET}%s  %s\n" "$title" "$date_display" "$steps_display"
          fi
        else
          if [[ -n "$search_query" ]]; then
            printf "    %s%s  %s\n" "$(_highlight "$search_query" "$title")" "$date_display" "$steps_display"
          else
            printf "    ${DIM}%s%s  %s${RESET}\n" "$title" "$date_display" "$steps_display"
          fi
        fi
        rendered=$((rendered + 1))
      done

      local remaining=$(( vis_count - scroll_top - rendered ))
      if (( remaining > 0 )); then
        printf "  ${DIM}▼ %d below${RESET}\n" "$remaining"
      else
        echo ""
      fi
    fi

    # Footer
    if [[ -n "$search_query" ]]; then
      printf "  ${DIM}Type to filter  Bksp Delete  Esc Clear  Enter Select${RESET}"
    else
      printf "  ${DIM}↑/↓ Navigate  Enter Select  Type to search  Tab Sort: %-6s  Esc/q Quit${RESET}" "$sort_mode"
    fi
  }

  _draw_picker

  while true; do
    IFS= read -rsn1 key

    case "$key" in
      $'\x1b')
        read -rsn1 -t 0.1 k2
        if [[ -z "$k2" ]]; then
          if [[ -n "$search_query" ]]; then
            search_query=""
            _apply_filter
            selected=0
          else
            _picker_cleanup; trap - EXIT INT; printf "\n"; exit 0
          fi
        else
          read -rsn1 -t 0.1 k3
          case "$k3" in
            A) (( vis_count > 0 )) && selected=$(( (selected - 1 + vis_count) % vis_count )) ;;
            B) (( vis_count > 0 )) && selected=$(( (selected + 1) % vis_count )) ;;
          esac
        fi
        ;;
      $'\x7f'|$'\b')
        if [[ -n "$search_query" ]]; then
          search_query="${search_query%?}"
          _apply_filter
        fi
        ;;
      $'\x15')  # Ctrl+U — clear search
        if [[ -n "$search_query" ]]; then
          search_query=""
          _apply_filter
          selected=0
        fi
        ;;
      $'\t')  # Tab — toggle sort
        if [[ "$sort_mode" == "date" ]]; then
          sort_mode="alpha"
        else
          sort_mode="date"
        fi
        local prev_ri=${vis_indices[$selected]:-0}
        _sort_items
        _apply_filter
        # Restore selection
        selected=0
        for (( si=0; si<vis_count; si++ )); do
          if [[ "${vis_indices[$si]}" -eq "$prev_ri" ]]; then
            selected=$si
            break
          fi
        done
        ;;
      "")  # Enter
        if (( vis_count > 0 )); then
          local chosen_ri=${vis_indices[$selected]}
          CHAIN_FILE="${all_paths[$chosen_ri]}"
          _picker_cleanup; trap - EXIT INT; echo ""
          return 0
        fi
        ;;
      [qQ])
        if [[ -z "$search_query" ]]; then
          _picker_cleanup; trap - EXIT INT; printf "\n"; exit 0
        else
          search_query+="$key"
          _apply_filter
        fi
        ;;
      [[:print:]])
        search_query+="$key"
        _apply_filter
        ;;
      *) continue ;;
    esac

    _draw_picker
  done
}

# No file: show the picker when we have a terminal, otherwise the help text.
if [[ -z "$CHAIN_FILE" ]]; then
  if $PICK_MODE || [[ -t 0 && -t 1 ]]; then
    if [[ ! -t 0 ]]; then
      echo "Error: interactive mode needs a terminal" >&2
      exit 1
    fi
    pick_chain_file
  else
    usage 0
  fi
fi

# Resolve the file argument: as given (from the repo root, where ./ospf put
# us), from the caller's directory, or as a bare name under docs/prompts/.
if [[ ! -f "$CHAIN_FILE" ]]; then
  for candidate in \
      "$CALLER_PWD/$CHAIN_FILE" \
      "$PROMPTS_DIR/$CHAIN_FILE" \
      "$PROMPTS_DIR/${CHAIN_FILE}-prompt.md" \
      "$PROMPTS_DIR/${CHAIN_FILE}.md"; do
    if [[ -f "$candidate" ]]; then
      CHAIN_FILE="$candidate"
      break
    fi
  done
fi

if [[ ! -f "$CHAIN_FILE" ]]; then
  echo "Error: file not found: $CHAIN_FILE" >&2
  exit 1
fi

# ─── Parse markdown chain file ─────────────────────────────────────────────

CHAIN_NAME=""
CHAIN_CWD=""
CHAIN_MODEL=""
CHAIN_EFFORT=""
CHAIN_PERMISSIONS=""
CHAIN_CATEGORY=""
CHAIN_PREFLIGHT=""

step_names=()
step_prompts=()
step_models=()
step_efforts=()
step_permissions=()
step_preflights=()

parse_md() {
  local file="$1"
  local section="header"  # header | meta | step
  local current_name=""
  local current_prompt=""
  local current_model=""
  local current_effort=""
  local current_permissions=""
  local current_preflight=""
  local in_step_meta=true

  while IFS= read -r line || [[ -n "$line" ]]; do
    # Chain name from H1
    if [[ "$section" == "header" && "$line" =~ ^#\ (.+) ]]; then
      CHAIN_NAME="${BASH_REMATCH[1]}"
      section="meta"
      continue
    fi

    # Chain-level metadata (between H1 and first H2)
    if [[ "$section" == "meta" ]]; then
      if [[ "$line" =~ ^##\ (.+) ]]; then
        current_name="${BASH_REMATCH[1]}"
        section="step"
        in_step_meta=true
        continue
      fi
      if [[ "$line" =~ ^([a-z_]+):\ *(.+) ]]; then
        local key="${BASH_REMATCH[1]}" val="${BASH_REMATCH[2]}"
        case "$key" in
          model)       CHAIN_MODEL="$val" ;;
          effort)      CHAIN_EFFORT="$val" ;;
          permissions) CHAIN_PERMISSIONS="$val" ;;
          cwd)         CHAIN_CWD="$val" ;;
          category)    CHAIN_CATEGORY="$val" ;;
          preflight)   CHAIN_PREFLIGHT="$val" ;;
        esac
      fi
      continue
    fi

    # Delimiter — finalize current step, start next
    if [[ "$line" =~ ^-----\[NEXT_PROMPT\]-----$ ]]; then
      _finalize_step
      current_name=""
      current_prompt=""
      current_model=""
      current_effort=""
      current_permissions=""
      current_preflight=""
      in_step_meta=true
      continue
    fi

    # Step heading
    if [[ "$section" == "step" && "$line" =~ ^##\ (.+) ]]; then
      current_name="${BASH_REMATCH[1]}"
      in_step_meta=true
      continue
    fi

    # Inside a step — parse metadata or accumulate prompt
    if [[ "$section" == "step" ]]; then
      if $in_step_meta; then
        if [[ -z "$line" ]]; then
          continue
        fi
        if [[ "$line" =~ ^([a-z_]+):\ *(.+) ]]; then
          local key="${BASH_REMATCH[1]}" val="${BASH_REMATCH[2]}"
          case "$key" in
            model)       current_model="$val" ;;
            effort)      current_effort="$val" ;;
            permissions) current_permissions="$val" ;;
            preflight)   current_preflight="$val" ;;
          esac
          continue
        fi
        in_step_meta=false
      fi
      if [[ -n "$current_prompt" ]]; then
        current_prompt+=$'\n'"$line"
      else
        current_prompt="$line"
      fi
    fi
  done < "$file"

  _finalize_step
}

_finalize_step() {
  [[ -z "$current_name" && -z "$current_prompt" ]] && return
  local trimmed
  trimmed=$(echo "$current_prompt" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
  local name="${current_name:-step-$((${#step_names[@]} + 1))}"
  step_names+=("$name")
  step_prompts+=("$trimmed")
  step_models+=("$current_model")
  step_efforts+=("$current_effort")
  step_permissions+=("$current_permissions")
  step_preflights+=("$current_preflight")
}

parse_md "$CHAIN_FILE"

# Resolve cwd metadata to an absolute path (relative values are taken from the
# repo root, not the invocation directory).
if [[ -n "$CHAIN_CWD" ]]; then
  [[ "$CHAIN_CWD" == "~"* ]] && CHAIN_CWD="${HOME}${CHAIN_CWD#\~}"
  [[ "$CHAIN_CWD" != /* ]] && CHAIN_CWD="$REPO_ROOT/$CHAIN_CWD"
  if [[ ! -d "$CHAIN_CWD" ]]; then
    echo "Error: cwd directory not found: $CHAIN_CWD" >&2
    exit 1
  fi
fi

CHAIN_NAME="${CHAIN_NAME:-chain}"
STEP_COUNT=${#step_names[@]}

if [[ "$STEP_COUNT" -eq 0 ]]; then
  echo "Error: no steps found in chain file" >&2
  exit 1
fi

# ─── Durable per-step state ─────────────────────────────────────────────────
#
# After every step, the status of all steps is written to a state file under
# tmp/chain-runs/, keyed by the chain file's absolute path. --resume reads it
# back and skips steps that completed in a previous run. The file is deleted
# once every step has completed.

CHAIN_FILE_ABS="$(cd "$(dirname "$CHAIN_FILE")" && pwd)/$(basename "$CHAIN_FILE")"
CHAIN_FILE_DISPLAY="${CHAIN_FILE_ABS#"$REPO_ROOT"/}"
STATE_DIR="$REPO_ROOT/tmp/chain-runs"
_path_hash=$(printf '%s' "$CHAIN_FILE_ABS" | shasum -a 256 | cut -c1-8)
_slug=$(basename "$CHAIN_FILE_ABS" .md | tr -c 'a-zA-Z0-9._\n-' '-')
STATE_FILE="$STATE_DIR/${_slug}-${_path_hash}.state"
CHAIN_HASH=$(shasum -a 256 "$CHAIN_FILE_ABS" | cut -c1-12)

prev_statuses=()

load_state() {
  [[ -f "$STATE_FILE" ]] || return 1
  local stored_hash num status _rest
  stored_hash=$(awk -F'\t' 'NR==1 {print $3}' "$STATE_FILE")
  while IFS=$'\t' read -r num status _rest; do
    [[ "$num" =~ ^[0-9]+$ ]] || continue
    prev_statuses[$((num - 1))]="$status"
  done < "$STATE_FILE"
  if [[ "$stored_hash" != "$CHAIN_HASH" ]]; then
    echo "${YELLOW}Warning: chain file changed since the saved run —" \
         "step numbering may have shifted.${RESET}"
  fi
  return 0
}

save_state() {
  $DRY_RUN && return 0
  mkdir -p "$STATE_DIR"
  {
    printf '#chain\t%s\t%s\t%s\n' "$CHAIN_FILE_ABS" "$CHAIN_HASH" "$STEP_COUNT"
    local i status
    for (( i=0; i<STEP_COUNT; i++ )); do
      status="${results[$i]:-pending}"
      [[ "$status" == "done (prev)" ]] && status="done"
      printf '%s\t%s\t%s\t%s\n' "$((i + 1))" "$status" "$(date +%s)" "${step_names[$i]}"
    done
  } > "$STATE_FILE"
}

# Decide whether to resume from saved state
if ! $DRY_RUN && ! $FRESH && [[ -f "$STATE_FILE" ]]; then
  if load_state; then
    _done_count=0
    _first_pending=0
    for (( i=0; i<STEP_COUNT; i++ )); do
      if [[ "${prev_statuses[$i]:-}" == "done" ]]; then
        _done_count=$((_done_count + 1))
      elif [[ "$_first_pending" -eq 0 ]]; then
        _first_pending=$((i + 1))
      fi
    done
    if [[ "$_done_count" -ge "$STEP_COUNT" ]]; then
      $RESUME && echo "All $STEP_COUNT steps already completed in the saved run — starting fresh."
      RESUME=false
      prev_statuses=()
    elif ! $RESUME && [[ "$_done_count" -gt 0 ]]; then
      if [[ -t 0 ]]; then
        printf "Previous run completed %d/%d steps. Resume from step %d? [Y/n] " \
          "$_done_count" "$STEP_COUNT" "$_first_pending"
        read -r _ans
        if [[ "$_ans" =~ ^[Nn] ]]; then
          prev_statuses=()
        else
          RESUME=true
        fi
      else
        echo "Note: saved state found ($_done_count/$STEP_COUNT steps done)." \
             "Pass --resume to skip completed steps, or --fresh to discard the state."
        prev_statuses=()
      fi
    fi
  fi
elif $RESUME && [[ ! -f "$STATE_FILE" ]]; then
  echo "No saved state for this chain — starting from step 1."
  RESUME=false
fi

# ─── Preflight checks ───────────────────────────────────────────────────────

# Run one preflight token. Silent on success; prints a fix hint and returns 1
# on failure.
run_one_check() {
  local token="$1"
  case "$token" in
    gh)
      if gh auth status >/dev/null 2>&1; then return 0; fi
      echo "gh CLI not authenticated — run: gh auth login"
      return 1 ;;
    cmd=*)
      local c="${token#cmd=}"
      if command -v "$c" >/dev/null 2>&1; then return 0; fi
      echo "command not found on PATH: $c"
      return 1 ;;
    file=*)
      local f="${token#file=}"
      [[ "$f" != /* ]] && f="$REPO_ROOT/$f"
      if [[ -e "$f" ]]; then return 0; fi
      echo "path does not exist: $f"
      return 1 ;;
    *)
      echo "unknown preflight token: $token (expected gh, cmd=NAME or file=PATH)"
      return 1 ;;
  esac
}

# Run all preflight tokens for a step, re-polling failures every 20s until
# PREFLIGHT_TIMEOUT. Returns 1 if any check is still failing at the deadline.
run_preflight() {
  local tokens_raw="$1"
  local -a tokens=()
  IFS=', ' read -r -a tokens <<< "$tokens_raw"
  local deadline=$(( $(date +%s) + PREFLIGHT_TIMEOUT ))

  while true; do
    local -a failures=()
    local t hint
    for t in "${tokens[@]}"; do
      [[ -z "$t" ]] && continue
      if ! hint=$(run_one_check "$t"); then
        failures+=("$t: $hint")
      fi
    done

    if [[ ${#failures[@]} -eq 0 ]]; then
      echo "  preflight: ok ($tokens_raw)"
      return 0
    fi

    echo "  ${YELLOW}preflight failing:${RESET}"
    local f
    for f in "${failures[@]}"; do
      echo "    ${YELLOW}- $f${RESET}"
    done

    local now wait_s
    now=$(date +%s)
    if [[ "$now" -ge "$deadline" ]]; then
      return 1
    fi
    wait_s=$(( deadline - now < 20 ? deadline - now : 20 ))
    echo "  ${DIM}re-checking in ${wait_s}s (gives up in $((deadline - now))s)...${RESET}"
    sleep "$wait_s"
  done
}

echo "Chain: $CHAIN_NAME ($STEP_COUNT steps)"
echo "File:  $CHAIN_FILE_DISPLAY"
if [[ "$START_FROM" -gt 1 ]]; then
  echo "Starting from step $START_FROM"
fi
if $RESUME; then
  echo "Resuming from saved state (completed steps will be skipped)"
fi
echo ""

# ─── Agent lifecycle ────────────────────────────────────────────────────────

# Read the fields of a job's state.json that decide whether it is still
# working, as one tab-separated line. Any parse failure prints nothing.
# Empty values are emitted as "-": tab is an IFS whitespace character, so a
# genuinely empty field would collapse and shift every field after it.
#
#   1 state      2 tempo       3 has_output  4 queued   5 busy_tasks
#   6 has_wake   7 live_fan    8 updatedAt   9 needs_you
#  10 block_qs  11 needs
read_job_state() {
  jq -r '
    def nonempty: if . == null then false
                  elif type == "object" or type == "array" then (length > 0)
                  elif type == "string" then (length > 0)
                  else true end;
    def dash: if . == null or . == "" then "-" else . end;
    [ (.state // "unknown"),
      (.tempo | dash),
      (if (.output | nonempty) then "yes" else "no" end),
      (.inFlight.queued // 0),
      ((.inFlight.tasks // 0) - (.inFlight.drainableMonitors // 0)),
      (if .inFlight.wake != null then "yes" else "no" end),
      ([ (.fan // [])[] | select(.doneAt == null) ] | length),
      (.updatedAt | dash),
      (if (.needs_you // false) then "yes" else "no" end),
      ((.block.questions // []) | length),
      (.needs | dash)
    ] | @tsv
  ' "$1" 2>/dev/null
}

# True when the harness has nothing left in flight for this job: not actively
# working, nothing queued, no undrained tasks, no scheduled self-wake and no
# live fan-out entry. This mirrors the CLI's own "settled" predicate.
#
# A background agent's terminal state is *inferred* from the wording of its
# final message (a regex pre-pass, then an LLM classifier). When neither
# resolves it, the job keeps the state it had while running — "working" — with
# no output, forever. Settled-and-unchanged is the signal that the agent has
# actually stopped, independent of how it phrased its last sentence.
job_is_settled() {
  local tempo="$1" queued="$2" busy="$3" wake="$4" live_fan="$5"
  [[ "$tempo" == "active" ]] && return 1
  [[ "${queued:-0}" -gt 0 ]] && return 1
  [[ "${busy:-0}" -gt 0 ]] && return 1
  [[ "$wake" == "yes" ]] && return 1
  [[ "${live_fan:-0}" -gt 0 ]] && return 1
  return 0
}

wait_for_agent() {
  local agent_name="$1"
  local agent_id="${2:-}"
  local blocked_since=0
  local blocked_warned=false
  local settled_since=0
  local settled_mark=""

  if ! command -v jq &>/dev/null; then
    echo "Error: jq is required for polling (brew install jq)" >&2
    return 1
  fi

  local state_json=""
  if [[ -n "$agent_id" ]]; then
    state_json="$HOME/.claude/jobs/$agent_id/state.json"
  else
    echo "  ${YELLOW}!! could not read the agent id from the launch output —" \
         "falling back to name matching${RESET}"
  fi

  while true; do
    sleep "$POLL_INTERVAL"

    local state="" tempo="" has_output="no" queued=0 busy=0 wake="no"
    local live_fan=0 updated="" needs_you="no" block_qs=0 needs=""
    local line=""

    if [[ -n "$state_json" && -f "$state_json" ]]; then
      line=$(read_job_state "$state_json")
    fi

    if [[ -n "$line" ]]; then
      IFS=$'\t' read -r state tempo has_output queued busy wake \
        live_fan updated needs_you block_qs needs <<<"$line"
    else
      # No readable state.json — fall back to the agents list, which only
      # carries the coarse state field.
      state=$(claude agents --json --all 2>/dev/null \
        | jq -r --arg name "$agent_name" '
            [.[] | select(.name == $name)] | last | .state // "unknown"
          ') || state="unknown"
      [[ -n "$state" ]] || state="unknown"
    fi

    # Primary signal: the agent produced a final answer. The harness only
    # writes .output when it classified the closing message as done or failed.
    if [[ "$has_output" == "yes" ]]; then
      echo "  -> completed"
      claude stop "$agent_id" &>/dev/null || true
      return 0
    fi

    case "$state" in
      done)
        echo "  -> completed"
        [[ -z "$agent_id" ]] || claude stop "$agent_id" &>/dev/null || true
        return 0 ;;
      failed)
        echo "  -> FAILED"
        return 1 ;;
      stopped)
        echo "  -> stopped by user"
        return 2 ;;
      unknown)
        blocked_since=0
        settled_since=0
        echo "  -> agent not found (may still be starting...)"
        continue ;;
      blocked)
        # "blocked" rarely means a permission prompt. It is mostly what the
        # classifier returns when the closing message reads like a question,
        # and it also covers transient rate limits and API errors that the
        # agent recovers from on its own — so keep waiting out the timeout.
        local now
        now=$(date +%s)
        if [[ "$blocked_since" -eq 0 ]]; then
          blocked_since=$now
        fi
        if ! $blocked_warned; then
          blocked_warned=true
          echo ""
          echo "  ${YELLOW}!! agent is blocked — check it via: claude agents" \
               "(auto-fails after ${BLOCKED_TIMEOUT}s)${RESET}"
          [[ "$needs" != "-" ]] && echo "  ${DIM}it needs: ${needs}${RESET}"
        fi
        if [[ $((now - blocked_since)) -ge "$BLOCKED_TIMEOUT" ]]; then
          echo ""
          echo "  ${RED}-> BLOCKED for over ${BLOCKED_TIMEOUT}s — marking step" \
               "failed. The agent is still blocked; resolve or stop it via:" \
               "claude agents${RESET}"
          return 1
        fi
        printf "\r  status: %-12s (waiting on input %ss/%ss — check: claude agents)" \
          "$state" "$((now - blocked_since))" "$BLOCKED_TIMEOUT"
        settled_since=0
        continue ;;
    esac

    blocked_since=0

    # Non-terminal state with nothing in flight. If that holds — with an
    # unchanged updatedAt — for SETTLE_TIMEOUT, the agent has finished and the
    # harness simply never reclassified its closing message.
    if [[ -n "$line" ]] && job_is_settled "$tempo" "$queued" "$busy" "$wake" "$live_fan"; then
      local mark="${state}|${tempo}|${updated}"
      local now
      now=$(date +%s)
      if [[ "$mark" != "$settled_mark" ]]; then
        settled_mark="$mark"
        settled_since=$now
      elif [[ $((now - settled_since)) -ge "$SETTLE_TIMEOUT" ]]; then
        echo ""
        echo "  ${GREEN}-> completed${RESET} ${DIM}(idle and unchanged for" \
             "${SETTLE_TIMEOUT}s while still reporting '${state}' — the harness" \
             "never reclassified the closing message)${RESET}"
        claude stop "$agent_id" &>/dev/null || true
        return 0
      fi
      printf "\r  status: %-12s (idle %ss/%ss — no work in flight)" \
        "$state" "$((now - settled_since))" "$SETTLE_TIMEOUT"
    else
      settled_since=0
      settled_mark=""
      printf "\r  status: %-12s" "$state"
    fi
  done
}

# ─── Run steps ──────────────────────────────────────────────────────────────

results=()

for (( i=0; i<STEP_COUNT; i++ )); do
  step_num=$((i + 1))

  if [[ "$step_num" -lt "$START_FROM" ]]; then
    results+=("skipped")
    continue
  fi

  step_name="${step_names[$i]}"
  step_prompt="${step_prompts[$i]}"
  model="${step_models[$i]:-$CHAIN_MODEL}"
  effort="${step_efforts[$i]:-$CHAIN_EFFORT}"
  permissions="${step_permissions[$i]:-$CHAIN_PERMISSIONS}"
  step_preflight="${step_preflights[$i]:-$CHAIN_PREFLIGHT}"

  if [[ -n "$CHAIN_CATEGORY" ]]; then
    agent_name="[${CHAIN_CATEGORY}] ${CHAIN_NAME} [${step_num}/${STEP_COUNT}] ${step_name}"
  else
    agent_name="${CHAIN_NAME} [${step_num}/${STEP_COUNT}] ${step_name}"
  fi

  # Resume: skip steps that completed in a previous run
  if $RESUME && [[ "${prev_statuses[$i]:-}" == "done" ]]; then
    echo "[$step_num/$STEP_COUNT] $step_name — done in previous run, skipping"
    results+=("done (prev)")
    continue
  fi

  echo "[$step_num/$STEP_COUNT] $step_name"

  if $DRY_RUN; then
    echo "  prompt: ${step_prompt:0:120}..."
    [[ -n "$model" ]] && echo "  model: $model"
    [[ -n "$effort" ]] && echo "  effort: $effort"
    [[ -n "$permissions" ]] && echo "  permissions: $permissions"
    [[ -n "$CHAIN_CWD" ]] && echo "  add-dir: $CHAIN_CWD"
    [[ -n "$step_preflight" ]] && echo "  preflight: $step_preflight"
    echo "  agent name: $agent_name"
    echo ""
    results+=("dry-run")
    continue
  fi

  max_attempts=$((RETRIES + 1))
  step_result=""

  for (( attempt=1; attempt<=max_attempts; attempt++ )); do
    if [[ -n "$step_preflight" ]] && ! $SKIP_PREFLIGHT; then
      if ! run_preflight "$step_preflight"; then
        step_result="preflight-failed"
        break
      fi
    fi

    attempt_name="$agent_name"
    if [[ "$attempt" -gt 1 ]]; then
      attempt_name="$agent_name (retry $((attempt - 1)))"
      echo "  launching... (attempt $attempt/$max_attempts)"
    else
      echo "  launching..."
    fi

    # --add-dir is variadic: if it is the last flag before the prompt, it
    # swallows the prompt as a directory path and the agent starts idle.
    # --name always follows it, so it can never sit adjacent to the prompt.
    cmd=(claude --bg)
    [[ -n "$CHAIN_CWD" ]] && cmd+=(--add-dir "$CHAIN_CWD")
    cmd+=(--name "$attempt_name")
    [[ -n "$model" ]] && cmd+=(--model "$model")
    [[ -n "$effort" ]] && cmd+=(--effort "$effort")
    [[ -n "$permissions" ]] && cmd+=(--permission-mode "$permissions")
    cmd+=("$step_prompt")

    launch_exit=0
    launch_output=$(cd "$REPO_ROOT" && "${cmd[@]}" 2>&1) || launch_exit=$?
    filtered_output=$(echo "$launch_output" | grep -v '^$')

    if [[ "$launch_exit" -ne 0 ]] || [[ -z "$filtered_output" ]]; then
      echo "  -> failed to launch agent" >&2
      [[ -n "$filtered_output" ]] && echo "$filtered_output" | sed 's/^/    /' >&2
      step_result="launch-failed"
      if [[ "$attempt" -lt "$max_attempts" ]]; then
        echo "  -> retrying..."
        continue
      fi
      break
    fi
    echo "$filtered_output"

    # Extract the agent ID from claude --bg output (first 8-char hex token)
    agent_id=$(echo "$filtered_output" | grep -oE '[0-9a-f]{8}' | head -1)

    if wait_for_agent "$attempt_name" "$agent_id"; then
      step_result="done"
      break
    else
      exit_code=$?
      if [[ "$exit_code" -eq 2 ]]; then
        # Stopped by the user — deliberate, so never auto-retry
        step_result="stopped"
        break
      fi
      step_result="failed"
      if [[ "$attempt" -lt "$max_attempts" ]]; then
        echo "  -> retrying (attempt $((attempt + 1))/$max_attempts)..."
      fi
    fi
  done

  results+=("$step_result")
  save_state

  if [[ "$step_result" == "preflight-failed" ]]; then
    echo "" >&2
    echo "${RED}Preflight still failing after ${PREFLIGHT_TIMEOUT}s — aborting chain.${RESET}" >&2
    echo "Fix the failing check above, then resume with:" >&2
    echo "  ./ospf chain \"$CHAIN_FILE_DISPLAY\" --resume" >&2
    break
  fi

  if [[ "$step_result" != "done" ]] && $STOP_ON_FAIL; then
    echo "Aborting chain (--stop-on-fail)" >&2
    break
  fi
  echo ""
done

# ─── Summary ────────────────────────────────────────────────────────────────

echo ""
echo "=== Chain Summary ==="
for (( i=0; i<STEP_COUNT; i++ )); do
  step_num=$((i + 1))
  status="${results[$i]:-not-run}"
  printf "  [%d] %-40s %s\n" "$step_num" "${step_names[$i]}" "$status"
done

failed_count=0
done_count=0
for r in "${results[@]}"; do
  case "$r" in
    failed|launch-failed|preflight-failed) ((failed_count++)) || true ;;
    done|"done (prev)") ((done_count++)) || true ;;
  esac
done

# Every step completed — the saved state is no longer needed
if ! $DRY_RUN && [[ "$done_count" -eq "$STEP_COUNT" ]]; then
  rm -f "$STATE_FILE"
fi

if [[ "$failed_count" -gt 0 ]]; then
  echo ""
  echo "$failed_count step(s) failed. Resume with: ./ospf chain \"$CHAIN_FILE_DISPLAY\" --resume"
  exit 1
fi
