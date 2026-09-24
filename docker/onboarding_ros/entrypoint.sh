#!/bin/bash
# Source ROS 2 (and a previous colcon install, if any) then exec.
# Used as the image ENTRYPOINT *and* as the prefix for
# `docker compose exec` so non-interactive commands see AMENT_*.
set -e
# shellcheck disable=SC1091
source /opt/ros/humble/setup.bash
if [ -f /ws/install/setup.bash ]; then
    # shellcheck disable=SC1091
    source /ws/install/setup.bash
fi
exec "$@"
