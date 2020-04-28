#!/bin/bash
xscreensaver -no-splash &
compton --backend glx --unredir-if-possible --vsync opengl-swc&
nm-applet&
