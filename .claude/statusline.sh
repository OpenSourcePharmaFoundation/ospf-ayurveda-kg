#!/bin/bash
input=$(cat)

# Extract fields
MODEL=$(echo "$input" | jq -r '.model.display_name' | sed 's/context/ctx/g; s/ (\(.*\))/: \1/g')
DIR=$(echo "$input" | jq -r '.workspace.current_dir')
PCT=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
DURATION_MS=$(echo "$input" | jq -r '.cost.total_duration_ms // 0')

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

# Line 1: model + folder + clock
echo -e "${PURPLE}[${MODEL}]${RESET} ${WHITE}📁 ${SHORT_DIR} | ⏱️  ${MINS}m ${SECS}s${RESET}"

# Line 2: progress bar + branch + repo link
if [ -n "$BRANCH" ]; then
  BRANCH_LINK="\033]8;;${REMOTE}/tree/${BRANCH}\a🌿 ${BRANCH}\033]8;;\a"
  printf '%b\n' "${BAR_COLOR}${BAR}${RESET} ${WHITE}${PCT}% | ${BRANCH_LINK}${REPO_LINK}${RESET}"
else
  printf '%b\n' "${BAR_COLOR}${BAR}${RESET} ${WHITE}${PCT}%${REPO_LINK}${RESET}"
fi
