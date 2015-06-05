__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window(600, 600)
window.set_caption('Perspective')

@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    # glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 3.0)
    gluPerspective(90.0, 1.0, 1.0, 30.0)
    glColor3f(1.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glScalef(0.5, 0.5, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex3f(0.0, 0.0, -1.0)
    glVertex3f(0.5, 0.0, -1.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3d(0, 0, -1)
    glVertex3d(0, 1, -1)
    glEnd()
    glFlush()

pg.app.run()
