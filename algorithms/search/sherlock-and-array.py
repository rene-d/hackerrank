# Algorithms > Search > Sherlock and Array
# Check whether there exists an element in the array such that sum of elements on its left is equal to the sum of elements on its right.
#
# https://www.hackerrank.com/challenges/sherlock-and-array/problem
# https://www.hackerrank.com/contests/101may14/challenges/sherlock-and-array
# challenge id: 2490
#


def solve(a):
    i = 0
    j = len(a) - 1
    l = r = 0

    while i < j:
        if l < r:
            l += a[i]
            i += 1
        else:
            r += a[j]
            j -= 1

    return "YES" if l == r else "NO"


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(a)
    print(result)