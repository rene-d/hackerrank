# Mathematics > Probability > Normal Distribution #3
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/normal-distribution-3/problem
# challenge id: 12846
#

from __future__ import print_function

try:
    from scipy.stats import norm

    f = norm(70, 10).cdf
    print("{:.2f}".format(100 - f(80) * 100))
    print("{:.2f}".format(100 - f(60) * 100))
    print("{:.2f}".format(f(60) * 100))

except ImportError:
    import math

    def phi(x, m, s):
        """ Cumulative Probability """
        return 1. / 2 * (1 + math.erf((x - m) / s / math.sqrt(2)))

    print("{:.2f}".format(100 - phi(60, 70, 10) * 100))
    print("{:.2f}".format(100 - phi(60, 70, 10) * 100))
    print("{:.2f}".format(phi(60, 70, 10) * 100))
