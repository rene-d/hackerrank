# Weekly Challenges - Week 5 > Closest Number
# What is the closest number?
#
# https://www.hackerrank.com/contests/w5/challenges/closest-number
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
