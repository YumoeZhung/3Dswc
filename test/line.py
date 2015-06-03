__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *
import math
import numpy

window = pyglet.window.Window()


@window.event
def on_draw():
    # glClearColor(0.0, 1.0, 0.0, 1.00)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    z = 0.0
    glBegin(GL_LINES)
    for angle in numpy.arange(0.0, 2 * 3.14 * 3, 0.5):
        x = 100.0 * math.cos(angle)
        y = 100.0 * math.sin(angle)
        print 200 + x, 200 + y
        glVertex3f(200.0, 200.0, 0.0)
        glVertex3f(200 + x, 200 + y, z)
        z += 1.0
    glEnd()


pyglet.app.run()