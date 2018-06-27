# Mathematics > Probability > Day 4: Normal Distribution #2
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/normal-distribution-2/problem
# https://www.hackerrank.com/contests/intro-to-statistics/challenges/normal-distribution-2
# challenge id: 12845
#

from __future__ import print_function
import math

def phi(x, m, s):
    """ Cumulative Probability """
    return 1. / 2 * (1 + math.erf((x - m) / s / math.sqrt(2)))

m, s = 20., 2.
print("{:.3f}".format(phi(19.5, m, s)))
print("{:.3f}".format(phi(22, m, s) - phi(20, m, s)))
