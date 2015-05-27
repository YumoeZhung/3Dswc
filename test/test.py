__author__ = 'Su Lei'

import pyglet

window1 = pyglet.window.Window()
context = window1.context
config = context.config
platform = pyglet.window.get_platform()
display = platform.get_default_display()

print display.get_default_screen()
