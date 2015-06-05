__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window()
window.set_caption('ModelView')

@window.event
def on_draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100.0, 100.0, -100.0, 100.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 10.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2d(0.0, 0.0)
    glVertex2d(0.0, 10.0)
    glVertex2d(10.0, 10.0)
    glVertex2d(10.0, 0.0)
    glEnd()
    glFlush()

pg.app.run()
