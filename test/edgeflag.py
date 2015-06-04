__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window(600, 600)
window.set_caption('edgeflag')
p = [-50.0, 50.0, 0.0, 125.0,
     50.0, 50.0, 125.0, 0.0,
     50.0, -50.0, 0.0, -125.0,
     -50.0, -50.0, -125.0, 0.0
     ]
points = (GLfloat * 16)(*p)
bFlag = False


@window.event
def on_draw():
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200.0, 200.0, -200.0, 200.0, -200.0, 200.0)
    glColor3f(1.0, 1.0, 0.0)
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glEdgeFlag(bFlag)
    glVertex2f(points[0], points[1])
    glVertex2f(points[4], points[5])
    glVertex2f(points[12], points[13])
    glVertex2f(points[4], points[5])
    glVertex2f(points[8], points[9])
    glVertex2f(points[12], points[13])
    glEdgeFlag(True)
    glVertex2f(points[0], points[1])
    glVertex2f(points[2], points[3])
    glEdgeFlag(bFlag)
    glVertex2f(points[4], points[5])
    glVertex2f(points[4], points[5])
    glEdgeFlag(True)
    glVertex2f(points[8], points[9])
    glVertex2f(points[6], points[7])
    glVertex2f(points[8], points[9])
    glVertex2f(points[10], points[11])
    glEdgeFlag(bFlag)
    glVertex2f(points[12], points[13])
    glVertex2f(points[12], points[13])
    glEdgeFlag(True)
    glVertex2f(points[0], points[1])
    glVertex2f(points[14], points[15])
    glEnd()
    glFlush()

pg.app.run()