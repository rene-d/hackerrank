"""
Find Angle MBC

https://www.hackerrank.com/challenges/find-angle/problem
"""

from math import atan2, pi

AB = int(input())
BC = int(input())

print(u"{}°".format(round(atan2(AB, BC) * 180 / pi)))
