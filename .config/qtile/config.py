# -*- coding: utf-8 -*-
import layouts
import keys
import widgets
import os
import pywal
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

mod = keys.mod

wallpaper_dir = os.path.expanduser('~/Pictures/Wallpaper')
# Set a random wallpaper using pywal
wallpaper = pywal.image.get(wallpaper_dir)
pywal.wallpaper.change(wallpaper)
theme = pywal.colors.get(wallpaper)

keys = keys.keys
group_names = ['\uf0ac' , '\uf0f6', '\uf120', '\uf07c', '\uf0c3', '\uf11b', '\uf085', '\uf0c0', '\uf0e4']
groups = [Group(i) for i in group_names]

for i, name in enumerate(group_names, 1):
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()

layouts = layouts.layouts

widget_defaults = widgets.defaults

screens = [
    Screen(top=bar.Bar(widgets.top(theme), size=20),
           bottom=bar.Bar(widgets.bottom(theme), size=20)),
    Screen()
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
