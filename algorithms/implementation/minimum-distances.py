# Minimum Distances
# Find the minimum distance between two different indices containing the same integers.
#
# https://www.hackerrank.com/challenges/minimum-distances/problem
#

import sys


def minimumDistances(a):

    b = [(v, i) for i, v in enumerate(a)]
    b = sorted(b)

    print('a=',a, file=sys.stderr)
    print('b=', b, file=sys.stderr)

    iprec = 0
    vprec = -1
    m = len(a)

    for v, i in b:
        if v == vprec:
            m = min(m, i - iprec)
        iprec = i
        vprec = v

    if m == len(a):
        m = -1
    return m


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
