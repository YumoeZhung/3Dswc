__author__ = 'Su Lei'

import pyglet
from pyglet.window import key

window = pyglet.window.Window()


@window.event
def on_key_press(symbol, modifiers):
    print symbol, modifiers
    print 'A key was pressed!'


@window.event
def on_draw():
    window.clear()

print key.I
pyglet.app.run()
