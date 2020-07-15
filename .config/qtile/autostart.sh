#!/bin/bash
dunst &
udiskie --smart-tray &
xscreensaver -no-splash &
compton --backend glx --unredir-if-possible --vsync opengl-swc&
nm-applet&
