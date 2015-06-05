__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *

window = pyglet.window.Window(600, 600)

@window.event
def on_draw():
    window.clear()
    glScissor(100, 100, 400, 400)
    glEnable(GL_SCISSOR_TEST)
    glClearColor(1.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glScissor(200, 200, 200, 200)
    glClearColor(1.0, 1.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 80, 0, 80, -1, 1)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(40, 40)
    glVertex2d(60, 40)
    glVertex2d(50, 50)
    glEnd()
    glFlush()

pyglet.app.run()