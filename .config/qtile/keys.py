import os
from libqtile.config import Key
from libqtile.command import lazy
mod = 'mod4'

TERM = os.getenv('TERM', 'xfce4-terminal')
EDITOR = os.getenv('EDITOR', TERM + '-e vim')
keys = [
    Key([mod], "k", lazy.layout.down(), desc='Switch to previous window in stack pane.'),
    Key([mod], "j", lazy.layout.up(), desc='Switch to next window in stack pane.'),
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc='Shuffle window down.'),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc='Shuffle window up.'),
    Key([mod], 'Tab', lazy.layout.next(), desc='Switch focus to next window in stack.'),
    Key([mod, "shift"], "space", lazy.layout.rotate(), desc='Swap panes of split stack.'),
    Key([mod], 'm', lazy.layout.grow(), desc='Enlarge pane on focus.'),
    Key([mod], 'b', lazy.layout.shrink(), desc='Shrink pane on focus.'),
    Key([mod], '0', lazy.layout.normalize(), desc='Restart the layout.'),
    # Sound
    #Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute"), desc='Volume down.'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute"), desc='Volume up.'),
    # Swap panes of split stack
    # Swap panes of split stack
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(TERM), desc='Start a terminal emulator.'),

    # Toggle between different layouts as defined below
    Key([mod], 'space', lazy.next_layout(), desc='Swap layout.'),
    Key([mod, 'shift'], 'space', lazy.window.toggle_floating(), desc='Toggle floating window.'),
    Key([mod], "x", lazy.window.kill(), desc='Close window.'),

    Key([mod], 'w', lazy.spawn('firefox'), desc='Launch web browser.'),
    Key([mod], 'e', lazy.spawn('{} -e ranger'.format(TERM)), desc='Launch file explorer.'),
    Key([mod], 't', lazy.spawn('gvim'), desc='Launch text editor.'),
    Key([mod, "control"], "r", lazy.restart(), desc='Restart qtile.'),
    Key([mod, "control"], "q", lazy.shutdown(), desc='Exit qtile.'),
    Key([mod], "r", lazy.spawncmd(), desc='Run a command.'),
    Key([mod], 'p', lazy.spawn('arandr'), desc='Launch screen configuration tool.'),
    Key([mod], 'l', lazy.spawn('xscreensaver-command -lock'), desc='Lock the screen')
]

