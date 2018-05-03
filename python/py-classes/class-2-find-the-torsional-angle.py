# Python > Classes > Class 2 - Find the Torsional Angle
# Find the angle between two planes.
#
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
#

import math
# (skeliton_head) ----------------------------------------------------------------------

class Points(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        """ produit scalaire """
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        """ produit vectoriel """
        return Points(self.y * no.z - self.z * no.y, 
                      self.z * no.x - self.x * no.z, 
                      self.x * no.y - self.y * no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __str__(self):
        return "[{} {} {}]".format(self.x, self.y, self.z)

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))

    if False:
        import numpy as np
        a = np.array(points[0])
        b = np.array(points[1])
        c = np.array(points[2])
        d = np.array(points[3])        
        x = np.cross(b - a, c - b)
        y = np.cross(c - b, d - c)
        angle = math.acos(x.dot(y) / (np.linalg.norm(x) * np.linalg.norm(y)))
        print("%.2f" % math.degrees(angle))
