# -*- coding: utf-8 -*-
import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import layouts
import keys
import widgets

mod = keys.mod

keys = keys.keys
group_names = [('\uf0ac', {'layout': 'monadtall'}),
               ('\uf0f6', {'layout': 'monadtall'}),
               ('\uf120', {'layout': 'monadtall'}),
               ('\uf07c', {'layout': 'monadtall'}),
               ('\uf0c3', {'layout': 'monadtall'}),
               ('\uf11b', {'layout': 'max'}),
               ('\uf085', {'layout': 'monadtall'}),
               ('\uf0c0', {'layout': 'monadtall'}),
               ('\uf0e4', {'layout': 'monadtall'})]
groups = [Group(name, **args) for name, args in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )
@hook.subscribe.startup_once
def autostart():
    subprocess.run([os.path.expanduser('~/.config/qtile/autostart.sh')],
                    check=False)  # Absence of the file or errors in it should not prevent qtile from starting.
 
@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()

layouts = layouts.layouts

widget_defaults = widgets.defaults

screens = [
    Screen(top=bar.Bar(widgets.top(), size=25)),
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
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Orage'},
    {'wmclass': 'VirtualBox Machine'},
    {'wmclass': 'Steam'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []
wmname = "LG3D"
