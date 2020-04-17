from libqtile import widget
defaults = dict(font='DroidSansMonoForPowerlinePlusNerdFileTypesMono',
                fontsize=12,
                padding=3)

def glyph(**kwargs):
    return widget.TextBox(text='\ue0ba', margin=0, fontsize=72, **kwargs)

def top(theme):
    return [
        glyph(foreground=theme['colors']['color6']),
        widget.GroupBox(margin_x=0, background=theme['colors']['color6'], foreground=theme['colors']['color8'], this_current_screen_border=theme['colors']['color4'], highlight_method='block', rounded=False, use_mouse_wheel=False, center_aligned=True),   # selected color 4, text 8
        glyph(background=theme['colors']['color6'], foreground='000000'),
        widget.WindowName(),
        widget.TextBox(text='\ue0ba', margin=0, fontsize=72, background='000000', foreground=theme['colors']['color2']),
        widget.CurrentLayoutIcon(background=theme['colors']['color2']),
        widget.CurrentLayout(background=theme['colors']['color2']),
        glyph(background=theme['colors']['color2'], foreground=theme['colors']['color4']),
        widget.CheckUpdates(background=theme['colors']['color4'], restart_indicator='⭮'),
        glyph(background=theme['colors']['color4'], foreground=theme['colors']['color5']),
        widget.Volume(emoji=True, background=theme['colors']['color5']),
        widget.Volume(emoji=False, background=theme['colors']['color5']),
        glyph(background=theme['colors']['color5'], foreground=theme['colors']['color3']),
        widget.TextBox(text='\uf0e7', background=theme['colors']['color3']),
        widget.Battery(background=theme['colors']['color3'], format='{char} {percent:2.0%}'),
        glyph(background=theme['colors']['color3'], foreground='000000'),

        widget.Systray(background=theme['colors']['color3']),
        widget.Notify(background=theme['colors']['color3']),
        widget.TextBox(text='\uf073'),
        widget.Clock(format='%a %H:%M %Y-%m-%d')
        ]

def bottom(theme):
    return [
        widget.Prompt(),
        widget.TaskList(),
        widget.Net(interface='wlp4s0'),
        ]
