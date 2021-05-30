#!/bin/bash
set -e

killall conky || echo "No conky processes found"
conky -c conky.conf

# Apply blur using the corresponding trick of the active window manager.
processes="$(xdotool search --class conky)"
for process in $processes;do
    if [[ -n "$(pgrep 'kwin')" ]];then
        xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id $process
    fi
done
