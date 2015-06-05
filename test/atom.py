__author__ = 'Su Lei'

import pyglet as pg
from pyglet.gl import *

window = pg.window.Window()
window.set_caption('Atom')


@window.event
def on_draw():
    fEffect = 0.0
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluPerspective(120.0, 1.0, 0.0, 1000.0)
    # glFrustum(-10.0, 10.0, -100.0, 100.0, 10.0, 2000.0)
    glOrtho(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, 70.0)
    glPointSize(20.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex3f(15.0, 15.0, 0.0)
    glEnd()
    glPushMatrix()
    glColor3f(0.0, 1.0, 1.0)
    glRotatef(fEffect, 0.0, 1.0, 0.0)
    glTranslatef(80.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(15.0, 15.0, 0.0)
    glEnd()
    glPopMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix()
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glRotatef(fEffect, 0.0, 1.0, 0.0)
    glTranslatef(80.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(15.0, 15.0, 0.0)
    glEnd()
    glPopMatrix()
    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glRotatef(-45.0, 0.0, 0.0, 1.0)
    glRotatef(fEffect, 0.0, 1.0, 0.0)
    glTranslatef(80.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(15.0, 15.0, 0.0)
    glEnd()
    glPopMatrix()
    glFlush()


pg.app.run()