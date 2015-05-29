__author__ = 'Su Lei'

class A():
    x = 10
    y = 20

a = A()
b = A()

print a.x, b.x

a.x = 200
print a.x, b.x