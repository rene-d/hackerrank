# Algorithms > Bit Manipulation > Maximizing XOR
# Given two integers, L and R, find the maximal value of A xor B,
# where A and B satisfy a condition.
#
# https://www.hackerrank.com/challenges/maximizing-xor/problem
#


# L   = 00000101......
# R   = 00000111......
# L^R = 00000010......
# sol = 0000001111...1      on met des 1 après le bit le plus à gauche de L^R


def maximizingXor(l, r):
    # Complete this function
    r = l ^ r
    m = 0
    while r != 0:
        r //= 2
        m = m * 2 + 1
    return m


if __name__ == "__main__":
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)
