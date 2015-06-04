__author__ = 'Su Lei'

from pyglet.gl import *
import pyglet

window = pyglet.window.Window(400, 400)


@window.event
def on_draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3.0)
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for x in (i * 0.1 for i in xrange(-50, 50)):
        y = x * x
        glVertex2f(x, y)
    glEnd()
    glFlush()
        

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5.0, 5.0, -5.0, 5.0, -1.0, 1.0)

pyglet.app.run()
