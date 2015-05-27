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


vertex_list = pyglet.graphics.vertex_list_indexed(2, [0, 0], ('v2i', (10, 15, 30, 35)),
                                                  ('c3B', (0, 0, 255, 0, 255, 0)))


@window.event
def on_draw():
    vertex_list.vertices[:2] = [60, 95]
    vertex_list.colors[:3] = [255, 0, 0]
    vertex_list.draw(pyglet.gl.GL_POINTS)


pyglet.app.run()



