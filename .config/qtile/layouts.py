from libqtile import layout

defaults = dict(border_focus='#00ffff',
                border_width=3,
                margin=10)
layouts = [layout.MonadTall(**defaults),
           layout.TreeTab(**defaults),
           layout.Matrix(**defaults),
           layout.Max()]

