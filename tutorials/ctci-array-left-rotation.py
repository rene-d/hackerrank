# Arrays: Left Rotation
# Given an array and a number, d, perform d left rotations on the array.
#
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
#


def array_left_rotation(a, n, k):
    k = k % n
    return a[k:] + a[:k]


n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
