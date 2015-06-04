__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *
import numpy as np
import math

window = pg.window.Window(400, 400)
window.set_caption('Cone')


@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100, 100, -100, 100, -100, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(45.0, 0.0, 1.0, 0.0)
    color = False
    glShadeModel(GL_FLAT)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 70.0)
    for i in np.arange(0.0, 3.14 * 2 + 0.1, 3.14 / 8):
        x = 50.0 * math.sin(i)
        y = 50.0 * math.cos(i)
        color = not color
        glVertex3f(x, y, 0.0)
        if color:
            glColor3f(1.0, 0.0, 0.0)
        else:
            glColor3f(0.0, 1.0, 1.0)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)
    for i in np.arange(0.0, 3.14 * 2 + 0.1, 3.14 / 8):
        x = 50.0 * math.sin(i)
        y = 50.0 * math.cos(i)
        color = not color
        glVertex2f(x, y)
        if color:
            glColor3f(1.0, 0.0, 0.0)
        else:
            glColor3f(0.0, 1.0, 1.0)
    glEnd()

pg.app.run()