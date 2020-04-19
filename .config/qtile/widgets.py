import os
import pywal
from libqtile import widget
defaults = dict(font='DroidSansMonoForPowerlinePlusNerdFileTypesMono',
                fontsize=16,
                padding=3)

wallpaper_dir = os.path.expanduser('~/Pictures/Wallpaper')
# Set a random wallpaper using pywal
wallpaper = pywal.image.get(wallpaper_dir)
pywal.wallpaper.change(wallpaper)
theme = pywal.colors.get(wallpaper)

def glyph_forward(**kwargs):
    return widget.TextBox(text='\ue0ba', margin=0, fontsize=60, **kwargs)

def glyph_backward(**kwargs):
    return widget.TextBox(text='\ue0be', margin=0, fontsize=60, **kwargs)

def top():
    return [
        glyph_backward(foreground=theme['colors']['color6']),
        widget.GroupBox(margin_x=0, background=theme['colors']['color6'], foreground=theme['colors']['color8'], this_current_screen_border=theme['colors']['color4'], highlight_method='block', rounded=False, use_mouse_wheel=False, center_aligned=True),   # selected color 4, text 8
        glyph_forward(background=theme['colors']['color6'], foreground='000000'),
        widget.WindowName(),
        glyph_backward(background='000000', foreground=theme['colors']['color2']),
        widget.CurrentLayoutIcon(background=theme['colors']['color2']),
        widget.CurrentLayout(background=theme['colors']['color2']),
        glyph_forward(background=theme['colors']['color2'], foreground=theme['colors']['color4']),
        widget.CheckUpdates(background=theme['colors']['color4'], restart_indicator='⭮'),
        glyph_forward(background=theme['colors']['color4'], foreground=theme['colors']['color5']),
        widget.Volume(emoji=True, background=theme['colors']['color5']),
        widget.Volume(emoji=False, background=theme['colors']['color5']),
        glyph_forward(background=theme['colors']['color5'], foreground=theme['colors']['color3']),
        widget.TextBox(text='\uf0e7', background=theme['colors']['color3']),
        widget.Battery(background=theme['colors']['color3'], format='{char} {percent:2.0%}'),
        widget.Systray(background=theme['colors']['color3']),
        widget.Clipboard(background=theme['colors']['color3']),
        glyph_forward(background=theme['colors']['color3'], foreground='000000'),
        widget.TextBox(text='\uf073'),
        widget.Clock(format='%a %H:%M %Y-%m-%d')
        ]

def bottom():
    return [
        widget.Prompt(),
        widget.TaskList(),
        widget.Notify(background=theme['colors']['color3']),
        widget.Net(interface='wlp4s0'),
        ]
