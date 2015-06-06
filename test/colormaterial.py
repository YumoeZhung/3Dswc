__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window(600, 600)
window.set_caption('ColorMaterial')

@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120, 1.0, 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    # glEnable(GL_LIGHTING)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.0, 0.0, -2.0)
    glVertex3f(1.0, 0.0, -2.0)
    glVertex3f(0.0, 1.0, -2.0)
    glEnd()
    glFlush()

pg.app.run()
