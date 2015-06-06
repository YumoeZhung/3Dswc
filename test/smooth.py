__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window(600, 600)
window.set_caption('Smooth')

@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120, 1.0, 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # ambient_light = (GLfloat * 3)(*(1.0, 1.0, 1.0))
    # red = (GLfloat * 4)(*(1.0, 0.0, 0.0, 1.0))
    glEnable(GL_LIGHTING)
    # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light)
    # glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
    glShadeModel(GL_FLAT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-1.0, 0.0, -2.0)
    glVertex3f(1.0, 0.0, -2.0)
    glVertex3f(0.0, 1.0, -2.0)
    glEnd()
    glFlush()

pg.app.run()
