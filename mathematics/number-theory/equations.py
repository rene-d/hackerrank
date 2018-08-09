# Mathematics > Number Theory > Equations
# Find the number of positive integral solutions for an equation.
#
# https://www.hackerrank.com/challenges/equations/problem
# challenge id: 39
#

# changement de variable:
# 1/x + 1/y = 1/n!              (1)
#   ⇒  (x+y)/(x∙y) = 1/n!
#   ⇒  n!(x+y) = x∙y
#   ⇒  xy - x∙n! - y∙n! + n!² = n!²
#   ⇒  (x - n!)(y - n!) = n!²
#   ⇒  x'∙y' = n!²

# donc le nombre de solutions de (1) est le nombre de diviseurs de n!²

primes = []
sieve = [True] * 1000001
for n in range(2, 1000001):
    if sieve[n]:
        primes.append(n)
        # supprime les mutiples de n
        for i in range(2 * n, 1000001, n):
            sieve[i] = False

# l'exposant de p premier dans n! est ep = ∑ n/p^i
# n! = ∏ p^ep
# le nombre de diviseurs de n! est donc ∏ (ep + 1)
# n!² = ∏ p^(2*ep)
# le nombre de diviseurs de n!² est donc ∏ (2*ep + 1)

n = int(input())
r = 1
for p in primes:
    ep = 0
    i = p
    while True:
        e = n // i
        if e == 0:
            break
        ep += e
        i *= p
    r *= (2 * ep + 1)
    r %= 1000007
print(r)
