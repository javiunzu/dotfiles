import os
from libqtile.config import Key
from libqtile.command import lazy
mod = 'mod4'

TERM = os.getenv('TERM', 'xterm')
EDITOR = os.getenv('EDITOR', TERM + '-e vim')
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(TERM)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "x", lazy.window.kill()),

    Key([mod], 'w', lazy.spawn('surf https://duckduckgo.com')),
    Key([mod], 'e', lazy.spawn('{} -e ranger'.format(TERM))),
    Key([mod], 't', lazy.spawn('gvim')),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], 'p', lazy.spawn('arandr'))
]

