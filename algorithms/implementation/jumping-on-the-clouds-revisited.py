# Jumping on the Clouds: Revisited
#  Determine the amount of energy Aerith has after the cloud game ends.
#
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
#

import sys

def jumpingOnClouds(c, k):
    # Complete this function
    return 100 - sum(c[i] * 2 + 1 for i in range(0, len(c), k))


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
