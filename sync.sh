#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <direction> [rclone options]"
    echo "Example: $0 push --progress --exclude '*.log'"
    echo "Example: $0 pull --progress"
    echo "Push will send to hassio, pull will get from hassio."
    exit 1
fi
direction=$1
shift || true # Remove direction from args

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
cd "${script_dir}"

remote_target="hassio-esphome:"
local_target="local-esphome:"
rclone_opts=(
    --filter '- **/.{git,esphome,pioenvs,piolibdeps}/'
    --filter '- /{lib,src}/'
    --filter '- /esphome/'
    --filter '- /.*'
    --filter '- /*.{sh,log,txt,ini}'
    --filter '+ /*.{yaml,yml}'
    --filter '+ /fonts/**'
    --filter '+ /external_components/**'
    --no-update-dir-modtime
)

if [[ "$direction" == "push" ]]; then
    echo "Pushing to hassio..."
    rclone sync -v "${rclone_opts[@]}" "$local_target" "$remote_target" "$@"
    exit $?
elif [[ "$direction" == "pull" ]]; then
    echo "Pulling from hassio..."
    rclone copy -v "${rclone_opts[@]}" "$remote_target" "$local_target" "$@"
    exit $?
else
    echo "Invalid direction: $direction"
    echo "Must be 'push' or 'pull'"
    exit 1
fi
