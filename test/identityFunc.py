__author__ = 'Su Lei'

from pyglet.gl import *
import pyglet

window = pyglet.window.Window()


@window.event
def on_draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-20.0, 20.0, -20.0, 20.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-0.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glEnd()
    glFlush()
    glTranslatef(3.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

pyglet.app.run()
