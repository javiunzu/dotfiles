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
    return widget.TextBox(text='\ue0b0', margin=0, padding=0, fontsize=20, **kwargs)

def glyph_backward(**kwargs):
    return widget.TextBox(text='\ue0b2', margin=0, padding=0, fontsize=20, **kwargs)

def battery(**kwargs):
    """ If there is a battery, add the proper widgets, otherwise just the termination glyph. """
    return [glyph_forward(background=theme['colors']['color3'], foreground=theme['colors']['color5']),
            widget.TextBox(text='\uf0e7', background=theme['colors']['color3']),
            widget.Battery(background=theme['colors']['color3'], format='{char} {percent:2.0%}'),
            glyph_forward(background='000000', foreground=theme['colors']['color3'])] if os.listdir('/sys/class/power_supply') else [glyph_forward(background='000000', foreground=theme['colors']['color5'])]

def top():
    widgets = [widget.Sep(padding=10, foreground='000000'),
               glyph_backward(foreground=theme['colors']['color6']),
               widget.GroupBox(margin_x=0, background=theme['colors']['color6'], foreground=theme['colors']['color8'], this_current_screen_border=theme['colors']['color4'], highlight_method='block', rounded=False, use_mouse_wheel=False, center_aligned=True),   # selected color 4, text 8
               glyph_forward(background='000000', foreground=theme['colors']['color6']),
               widget.WindowName(),
               glyph_backward(background='000000', foreground=theme['colors']['color2']),
               widget.CurrentLayoutIcon(background=theme['colors']['color2']),
               glyph_forward(background=theme['colors']['color5'], foreground=theme['colors']['color2']),
               widget.Volume(emoji=True, background=theme['colors']['color5']),
               widget.Volume(emoji=False, background=theme['colors']['color5'])]
    widgets.extend(battery())
    widgets.extend([widget.Sep(padding=10, foreground='000000'),
                    widget.Sep(padding=10, foreground='000000'),
                    widget.Systray(),
                    widget.Clipboard(background=theme['colors']['color3']),
                    widget.TextBox(text='\uf073'),
                    widget.Clock(format='%a %H:%M %Y-%m-%d')])
    return widgets

