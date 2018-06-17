# Mathematics > Number Theory > Akhil and GF
# Help Akhil in impressing his girlfriend
#
# https://www.hackerrank.com/challenges/akhil-and-gf/problem
# https://www.hackerrank.com/contests/infinitum-aug14/challenges/akhil-and-gf
# challenge id: 2324
#

for _ in range(int(input())):
    n, m = map(int, input().split())

    # 1111...11 = (10^n - 1) / 9
    # 1111...11 mod m = ((10^n - 1) / 9) mod m
    #                 = ((10^n mod (m * 9)) - 1) / 9

    p = pow(10, n, m * 9)
    print((p - 1) // 9)
