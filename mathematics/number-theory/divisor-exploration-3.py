# Mathematics > Number Theory > Divisor Exploration 3
# Find the value given at the root of a tree constructing by the given rules.
#
# https://www.hackerrank.com/challenges/divisor-exploration-3/problem
# https://www.hackerrank.com/contests/infinitum18/challenges/divisor-exploration-3
# challenge id: 12630
#


MOD = 1000000007


# compute the 1000 first primes
PRIME_1000 = 7919           # 7919 is the 1000th prime
primes = []
sieve = [True] * (1 + PRIME_1000)
for n in range(2, PRIME_1000 + 1):
    if sieve[n]:
        # by default, n is prime and add it to the list
        primes.append(n)
        # remove the multiples of n
        for i in range(n, PRIME_1000 + 1, n):
            sieve[i] = False


def binomial(n, k):
    """ binomial coefficient """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    den = 1
    for i in range(1, min(k, n - k) + 1):   # take advantage of symmetry
        num *= (n + 1 - i)
        den *= i
    c = num // den
    return c


def f(i, p, a):

    # f(1,p,a) = p^a
    # f(i,p,a) = (p * f(i-1,p,a) - binomial(a+i-2,i-2)) / (p-1)  for i >= 2

    num = p ** a
    for j in range(2, i + 1):
        num = p * num - binomial(a + j - 2, j - 2)
        num //= p - 1

    # print("    f({} {} {}) = {}".format(i, p, a, num))
    return num % MOD


def egcd(b, a):
    """ algortihme d'Euclide étendu: (g, x, y) tel que ax + by = g = gcd(a, b) """
    # https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_étendu
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def modinv(a, m):
    """ modular inverse avec Bachet-Bézout """
    # https://fr.wikipedia.org/wiki/Théorème_de_Bachet-Bézout
    g, x, _ = egcd(a, m)
    assert g == 1
    return x % m


def fast_f(i, p, a):

    # f(1,p,a) = p^a
    # f(i,p,a) = (p * f(i-1,p,a) - binomial(a+i-2,i-2)) / (p-1)  for i >= 2

    num, den = pow(p, a, MOD), 1
    c_num, c_den = 1, 1
    for j in range(2, i + 1):
        if j > 2:
            # compute the binomial coef
            c_num = (c_num * (a + j - 2)) % MOD
            c_den = (c_den * (j - 2)) % MOD
        num = (p * num * c_den  - c_num * den) % MOD
        den = (den * (p - 1) * c_den) % MOD

    num = (num * modinv(den, MOD)) % MOD

    #print("    f({} {} {}) = {}".format(i, p, a, num))
    return num


def solve(m, a, d):

    # R = ∏ f(d,pᵢ,a+i)

    res = 1
    for i in range(m):
        #x = f(d, primes[i], a + i + 1) % MOD
        x = fast_f(d, primes[i], a + i + 1) % MOD
        res *= x
        res %= MOD

    return res


#assert solve(2,0,1) == 18
#assert solve(2,0,2) == 39
#assert solve(1,0,3) == 4

for _ in range(int(input())):
    m, a, d = map(int, input().split())
    # 1 <= m, a, d <= 1000

    print(solve(m, a, d))
