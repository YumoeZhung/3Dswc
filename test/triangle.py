__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *

def draw_triangle():
    glBegin(GL_LINE_LOOP)
    glVertex2d(200, 100)
    glVertex2d(200, 300)
    glVertex2d(300, 250)
    glEnd()
    pass

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    draw_triangle()

    glEnable(GL_LINE_STIPPLE)

    glLineStipple(1, 0xF0F0)
    glLoadIdentity()
    glTranslatef(-20.0, 0.0, 0.0)
    draw_triangle()

    glLineStipple(1, 0xF00F)
    glLoadIdentity()
    glScalef(1.5, 1.0, 1.0)
    draw_triangle()

    glLineStipple(1, 0x8888)
    glLoadIdentity()
    glRotatef(30.0, 0.0, 0.0, 1.0)
    draw_triangle()

    glDisable(GL_LINE_STIPPLE)

pyglet.app.run()


