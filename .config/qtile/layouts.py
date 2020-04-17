from libqtile import layout
layouts = [layout.MonadTall(margin=5, border_focus='#00ffff'),
    layout.TreeTab(border_width=3),
    layout.Stack(num_stacks=2, border_width=3, border_focus='#00ffff', margin=5)]
