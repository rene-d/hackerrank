# Left Rotation
# Given an array and a number, d, perform d left rotations on the array.
#
# https://www.hackerrank.com/challenges/array-left-rotation/problem
#

def rotate(l, n):
    n = n % len(l)
    return l[n:] + l[:n]


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().split()))
    a = rotate(a, d)
    print(' '.join(map(str, a)))
