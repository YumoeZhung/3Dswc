__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
a = 5.0
a = GLfloat(a)

@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glLineStipple(2, 0x0101)
    glEnable(GL_LINE_STIPPLE)
    glBegin(GL_LINES)
    glVertex2i(100, 100)
    glVertex2i(200, 300)
    glEnd()
    glFlush()
    # glBegin(GL_LINE_STRIP)
    # glVertex3i(10, 10, 0)
    # glVertex3i(20, 20, 0)
    # glVertex3i(100, 100, 0)
    # glEnd()
    # glPointSize(a)
    # glBegin(GL_POINTS)
    # glVertex3i(10, 10, 0)
    # glVertex3i(20, 20, 0)
    # glVertex3i(100, 100, 1)
    # glEnd()
    # glFlush()

pyglet.app.run()
