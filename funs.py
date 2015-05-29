__author__ = 'Su Lei'


class Point():
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
        for j in xrange(1, len(s)):
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


def readSwc(fname):
    f = open('test.swc', 'r')
    pointsArray = []
    for i in f:
        p = Point(i)
        pointsArray.append(p)
    return pointsArray