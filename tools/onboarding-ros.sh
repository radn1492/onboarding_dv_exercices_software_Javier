#!/usr/bin/env bash
# Open a ROS 2 Humble shell for onboarding exercises 01–07 Phase A.
# Does not start the sim / pipeline stack.
#
# Usage (from anywhere):
#   tools/onboarding-ros.sh                 # interactive bash
#   tools/onboarding-ros.sh <cmd...>        # run a command with ROS sourced
#
# Examples:
#   tools/onboarding-ros.sh
#   tools/onboarding-ros.sh colcon build --symlink-install --packages-select hello_onboarding
#   tools/onboarding-ros.sh bash -lc 'cd /ws/src/04_plane_from_3_points && pytest -q'

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMPOSE=(docker compose -f "$ROOT/docker-compose.onboarding.yml")
cd "$ROOT"

if ! "${COMPOSE[@]}" ps --status running --services 2>/dev/null | grep -qx onboarding_ros; then
    echo "→ starting onboarding_ros"
    "${COMPOSE[@]}" up -d --build
fi
if [[ $# -eq 0 ]]; then
    export MSYS2_ARG_CONV_EXCL="/entrypoint.sh"
    exec "${COMPOSE[@]}" exec onboarding_ros /entrypoint.sh bash
fi
export MSYS2_ARG_CONV_EXCL="/entrypoint.sh"
exec "${COMPOSE[@]}" exec onboarding_ros "$@"
