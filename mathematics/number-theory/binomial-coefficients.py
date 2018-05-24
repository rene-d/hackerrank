# Mathematics > Number Theory > Binomial Coefficients
# Calculate how many binomial coefficients of n become 0 after modulo by P.
#
# https://www.hackerrank.com/challenges/binomial-coefficients/problem
# challenge id: 107
#

# corollaire du théorème de Lucas https://en.wikipedia.org/wiki/Lucas%27s_theorem

def solve(n, p):
    a = 1

    n1 = n + 1
    while n >= p:
        n, r = divmod(n, p)
        a *= r + 1
    a *= n + 1
    a = n1 - a
    print(a)


for _ in range(int(input())):
    n, p = map(int, input().split())
    solve(n, p)
