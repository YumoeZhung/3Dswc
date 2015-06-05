__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *
import numpy as np
import math

window = pg.window.Window(600, 600)
window.set_caption('Stencil')


@window.event
def on_draw():
    dR = 0.1
    cS = GLint(0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearStencil(cS)
    glClear(GL_COLOR_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100.0, 100.0, -100.0, 100.0, -10.0, 10.0)
    glColor3f(0.0, 1.0, 0.0)
    glEnable(GL_STENCIL_TEST)
    glStencilFunc(GL_NEVER, 0x0, 0x0)
    glStencilOp(GL_INCR, GL_INCR, GL_INCR)
    glBegin(GL_LINE_STRIP)
    for dA in np.arange(0.0, 400.0, 0.1):
        glVertex2d(dR * math.cos(dA), dR * math.sin(dA))
        dR *= 1.002
    glEnd()
    glStencilFunc(GL_NOTEQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    glRectf(0, 0, 50.0, 50.0)
    glFlush()

pg.app.run()


