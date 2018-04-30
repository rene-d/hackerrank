# Mathematics > Number Theory > Closest Number
# What is the closest number?
#
# https://www.hackerrank.com/challenges/closest-number/problem
#

def closestNumber(a, b, x):
    p = int(a ** b)
    m = (p // x) * x
    if p - m > m + x - p:
        return m + x
    else:
        return m


if __name__ == '__main__':
    for _ in range(int(input())):
        a, b, x = map(int, input().split())
        result = closestNumber(a, b, x)
        print(result)