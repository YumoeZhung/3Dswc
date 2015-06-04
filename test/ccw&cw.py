__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *


window = pg.window.Window()
window.set_caption('ccw&cw')

@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-150.0, 150.0, -150.0, 150.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPolygonMode(GL_BACK, GL_LINE)
    glPolygonMode(GL_FRONT, GL_FILL)
    glFrontFace(GL_CW)                                    # clockwise
    glBegin(GL_TRIANGLES)

    glVertex2f(0.0, 0.0)
    glVertex2f(25.0, 25.0)
    glVertex2f(50.0, 0.0)
    glEnd()
    glFrontFace(GL_CCW)                                   # anti-clockwise
    glBegin(GL_TRIANGLES)
    glVertex2f(-50.0, 0.0)
    glVertex2f(-75.0, 50.0)
    glVertex2f(-25.0, 0.0)
    glEnd()


pyglet.app.run()