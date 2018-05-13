# Mathematics > Geometry > Sherlock and Planes
# Help Sherlock with points on planes.
#
# https://www.hackerrank.com/challenges/sherlock-and-planes/problem
# https://www.hackerrank.com/contests/infinitum-may14/challenges/sherlock-and-planes
#

# je n'ai pas tout à faire le droit à numpy mais je me l'octroie !!!
import sys
sys.path += ['/var/ml/python3/lib/python3.5/site-packages']
import numpy


for _ in range(int(input())):
    # lit les quatre points A,B,C,D
    A = numpy.array(input().split(), numpy.int)
    B = numpy.array(input().split(), numpy.int)
    C = numpy.array(input().split(), numpy.int)
    D = numpy.array(input().split(), numpy.int)

    v = numpy.cross(B - A, C - A)
    w = numpy.dot(D - A, v)
    if w == 0: print("YES")
    else: print("NO")
