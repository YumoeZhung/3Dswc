__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *

import funs


points = funs.readSwc('test.swc')
window = pyglet.window.Window(1000, 600)
pyglet.app.run()