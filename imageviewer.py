__author__ = 'Su Lei'

import pyglet

window = pyglet.window.Window()
image = pyglet.image.load('test.jpg')


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)


pyglet.app.run()

