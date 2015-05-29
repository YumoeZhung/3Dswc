__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *


window = pyglet.window.Window()
# vertices = [0, 0, window.width, 0, window.width, window.height]
# vertices_gl = (GLfloat * len(vertices))(*vertices)
# print GLfloat * len(vertices)
# print vertices_gl
# print GLfloat * 100
# glEnableClientState(GL_VERTEX_ARRAY)
# glVertexPointer(2, GL_FLOAT, 0, vertices_gl)
#
#


#
# @window.event
# def on_resize(width, height):
# glViewport(0, 0, width, height)
# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
# gluPerspective(65, width / float(height), .1, 1000)
# glMatrixMode(GL_MODELVIEW)
# return pyglet.event.EVENT_HANDLED
#
#
#
#
# vertex_list = pyglet.graphics.vertex_list_indexed(2, [0, 0], ('v2i', (10, 15, 30, 35)),
#                                                   ('c3B', (0, 0, 255, 0, 255, 0)))
#
#
# @window.event
# def on_draw():
#     vertex_list.vertices[:2] = [60, 95]
#     vertex_list.colors[:3] = [255, 0, 0]
#     vertex_list.draw(pyglet.gl.GL_POINTS)

color_list = [1.0, 0.0, 0.0]
color_list_gl = (GLfloat * len(color_list))(*color_list)

@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glColor3fv(color_list_gl)
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2i(20, 20)
    glVertex2i(25, 80)
    glVertex2i(50, 87)
    glVertex2i(74, 12)
    glEnd()
    glFlush()


pyglet.app.run()



