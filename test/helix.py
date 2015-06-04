__author__ = 'Su Lei'

import pyglet as pg
import math
from pyglet.gl import *

window = pg.window.Window(400, 400)
window.set_caption('Helix')
dR = 1.0
dA = 0.0

@window.event
def on_draw():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100.0, 100.0, -100.0, 100.0, -10.0, 10.0)


def renderScene(dT):
    global dA, dR
    if dA - 0.0 < 0.00001:
        window.clear()
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    glVertex2f(dR * math.cos(dA), dR * math.sin(dA))
    print (dR * math.cos(dA), dR * math.sin(dA))
    glEnd()
    dR *= 1.01
    dA += 0.1
    if dA > 30.0:
        dR = 0.1
        dA = 0.0
    print dR, dA
    glFlush()

pg.clock.schedule_interval(renderScene, 0.01)
pg.app.run()


