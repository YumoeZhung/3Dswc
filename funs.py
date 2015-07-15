__author__ = 'Su Lei'


class SwcPoint():
    def __init__(self, s):
        self.data = self.s2l(s)
        self.seq = self.data[0]
        self.x = self.data[2]
        self.y = self.data[3]
        self.z = self.data[4]
        self.r = self.data[5]
        self.sup = self.data[6]

    def s2l(self, s):
        data = []
        x = ''
        for j in xrange(0, len(s)):
            if s[j] is ' ' or j is len(s) - 1:
                data.append(x)
                x = ''
            else:
                x += s[j]
        for k in xrange(len(data)):
            if k is 0 or k is 1 or k is 6:
                data[k] = int(data[k])
            else:
                data[k] = float(data[k])
        return data

    def l2d(self, l):
        d = {'seq': l[0], 'x': l[2], 'y': l[3], 'z': l[4], 'r': l[5], 'sup': l[6]}
        return d


class Line():
    def __init__(self):
        self.point_num = 0
        self.point_data = []

class Swc():
    def __init__(self, filename):
        self.points = self.readPointsFromSwc(filename)

    def readPointsFromSwc(self, fname):
        f = open(fname, 'r')
        pointsArray = []
        for i in f:
            p = SwcPoint(i)
            pointsArray.append(p)
        return pointsArray

    def readLinesFromSwc(self):
        point_num = len(self.points)
        for i in xrange(point_num):
            this_point = self.points[i]



