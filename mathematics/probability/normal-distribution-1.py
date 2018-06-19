# Mathematics > Probability > Day 4: Normal Distribution #1
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/normal-distribution-1/problem
# https://www.hackerrank.com/contests/intro-to-statistics/challenges/normal-distribution-1
# challenge id: 12844
#

from __future__ import print_function
import math

def phi(x, m, s):
    """ Cumulative Probability """
    return 1. / 2 * (1 + math.erf((x - m) / s / math.sqrt(2)))

m, s = 30., 4.
print("{:.3f}".format(phi(40, m, s)))
print("{:.3f}".format(1 - phi(21, m, s)))
print("{:.3f}".format(phi(35, m, s) - phi(30, m, s)))
