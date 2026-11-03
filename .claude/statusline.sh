#!/bin/bash
input=$(cat)

# Extract fields
MODEL=$(echo "$input" | jq -r '.model.display_name' | sed 's/context/ctx/g; s/ (\(.*\))/: \1/g')
DIR=$(echo "$input" | jq -r '.workspace.current_dir')
PCT=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
DURATION_MS=$(echo "$input" | jq -r '.cost.total_duration_ms // 0')
COST=$(echo "$input" | jq -r '.cost.total_cost_usd // 0')
LINES_ADDED=$(echo "$input" | jq -r '.cost.total_lines_added // 0')
LINES_REMOVED=$(echo "$input" | jq -r '.cost.total_lines_removed // 0')
RATE_5H=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')
RATE_7D=$(echo "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty')
EFFORT=$(echo "$input" | jq -r '.effort.level // empty')

# Persist the rate-limit windows so tools that don't get statusline stdin
# can show them. Atomic write so readers never see a partial file.
RATE_CACHE="$HOME/.claude/aiw-rate-limits.json"
RATE_JSON=$(echo "$input" | jq -c '.rate_limits // empty' 2>/dev/null)
if [ -n "$RATE_JSON" ] && [ "$RATE_JSON" != "{}" ]; then
  SESSION_ID=$(echo "$input" | jq -r '.session_id // empty')
  RATE_TMP="${RATE_CACHE}.tmp.$$"
  if jq -nc --argjson rl "$RATE_JSON" --arg sid "$SESSION_ID" \
      '{rate_limits: $rl, updated_at: now | floor, session_id: $sid}' \
      > "$RATE_TMP" 2>/dev/null; then
    mv -f "$RATE_TMP" "$RATE_CACHE" 2>/dev/null || rm -f "$RATE_TMP"
  else
    rm -f "$RATE_TMP"
  fi
fi

# Colors
WHITE='\033[97m'
PURPLE='\033[35m'
CYAN='\033[36m'
GREEN='\033[32m'
YELLOW='\033[33m'
RED='\033[31m'
RESET='\033[0m'

# Directory: show last 2 path components (current + 1 parent)
IFS='/' read -ra PARTS <<< "$DIR"
NUM=${#PARTS[@]}
if [ "$NUM" -ge 2 ]; then
  SHORT_DIR="${PARTS[$((NUM-2))]}/${PARTS[$((NUM-1))]}"
else
  SHORT_DIR="${DIR##*/}"
fi

# Duration
MINS=$((DURATION_MS / 60000))
SECS=$(((DURATION_MS % 60000) / 1000))

# Cost
COST_FMT=$(printf '$%.2f' "$COST")

# Git branch + remote
BRANCH=""
REPO_LINK=""
cd "$DIR" 2>/dev/null && BRANCH=$(git branch --show-current 2>/dev/null)
REMOTE=$(git remote get-url origin 2>/dev/null | sed 's/git@github.com:/https:\/\/github.com\//' | sed 's/\.git$//')
if [ -n "$REMOTE" ]; then
  REPO_NAME=$(basename "$REMOTE")
  REPO_LINK=" | ${CYAN}\033]8;;${REMOTE}\a🔗 ${REPO_NAME}\033]8;;\a${RESET}"
fi

# Progress bar color
if [ "$PCT" -ge 90 ]; then BAR_COLOR="$RED"
elif [ "$PCT" -ge 70 ]; then BAR_COLOR="$YELLOW"
else BAR_COLOR="$GREEN"; fi

# Build progress bar (10 chars)
FILLED=$((PCT / 10))
EMPTY=$((10 - FILLED))
BAR=""
[ "$FILLED" -gt 0 ] && printf -v FILL "%${FILLED}s" && BAR="${FILL// /█}"
[ "$EMPTY" -gt 0 ] && printf -v PAD "%${EMPTY}s" && BAR="${BAR}${PAD// /░}"

# Lines changed
LINES_BLOCK=""
if [ "$LINES_ADDED" -gt 0 ] || [ "$LINES_REMOVED" -gt 0 ]; then
  LINES_BLOCK=" | ${GREEN}+${LINES_ADDED}${RESET}/${RED}-${LINES_REMOVED}${RESET}"
fi

# Rate limit usage (5h session + 7d weekly)
RATE_BLOCK=""
if [ -n "$RATE_5H" ]; then
  RATE_INT=$(printf '%.0f' "$RATE_5H")
  if [ "$RATE_INT" -ge 90 ]; then
    RATE_BLOCK=" | ${RED}[5h ${RATE_INT}%]${RESET}"
  elif [ "$RATE_INT" -ge 70 ]; then
    RATE_BLOCK=" | ${YELLOW}[5h ${RATE_INT}%]${RESET}"
  else
    RATE_BLOCK=" | ${GREEN}[5h ${RATE_INT}%]${RESET}"
  fi
fi
if [ -n "$RATE_7D" ]; then
  WEEK_INT=$(printf '%.0f' "$RATE_7D")
  if [ "$WEEK_INT" -ge 90 ]; then
    RATE_BLOCK="${RATE_BLOCK} ${RED}[7d ${WEEK_INT}%]${RESET}"
  elif [ "$WEEK_INT" -ge 70 ]; then
    RATE_BLOCK="${RATE_BLOCK} ${YELLOW}[7d ${WEEK_INT}%]${RESET}"
  else
    RATE_BLOCK="${RATE_BLOCK} ${GREEN}[7d ${WEEK_INT}%]${RESET}"
  fi
fi

# Effort level badge
EFFORT_BLOCK=""
if [ -n "$EFFORT" ]; then
  case "$EFFORT" in
    low)    EFFORT_BLOCK=" | ${GREEN}⚡ ${EFFORT}${RESET} |" ;;
    medium) EFFORT_BLOCK=" | ${YELLOW}⚡ ${EFFORT}${RESET} |" ;;
    high)   EFFORT_BLOCK=" | ${CYAN}⚡ ${EFFORT}${RESET} |" ;;
    xhigh)  EFFORT_BLOCK=" | ${PURPLE}⚡ ${EFFORT}${RESET} |" ;;
    max)    EFFORT_BLOCK=" | ${RED}⚡ ${EFFORT}${RESET} |" ;;
    *)      EFFORT_BLOCK=" | ⚡ ${EFFORT} |" ;;
  esac
fi

# Line 1: model + effort + folder + cost + clock
echo -e "${PURPLE}[${MODEL}]${RESET}${EFFORT_BLOCK} ${WHITE}📁 ${SHORT_DIR} | ${COST_FMT} | ⏱️  ${MINS}m ${SECS}s${RESET}"

# Line 2: progress bar + lines + branch + repo link + rate limits
if [ -n "$BRANCH" ]; then
  BRANCH_LINK="\033]8;;${REMOTE}/tree/${BRANCH}\a🌿 ${BRANCH}\033]8;;\a"
  printf '%b\n' "${BAR_COLOR}${BAR}${RESET} ${WHITE}${PCT}%${LINES_BLOCK} | ${BRANCH_LINK}${REPO_LINK}${RATE_BLOCK}${RESET}"
else
  printf '%b\n' "${BAR_COLOR}${BAR}${RESET} ${WHITE}${PCT}%${LINES_BLOCK}${REPO_LINK}${RATE_BLOCK}${RESET}"
fi
