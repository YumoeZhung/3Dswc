__author__ = 'Su Lei'

import re

r = "[j-p]{1,2}"
rex = re.compile(r)
rex.match('ooooooooo')
print rex.groups
a = re.match(r, 'nn')
print a.group()