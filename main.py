__author__ = 'Su Lei'

import pyglet
from pyglet.gl import *
import funs


swc1 = funs.Swc('test.swc')
points = swc1.points
print points[0].x
