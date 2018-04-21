# Mathematics > Fundamentals > Is Fibo
# Find out if a number is a Fibonacci Number or not.
#
# https://www.hackerrank.com/challenges/is-fibo/problem
#

import bisect

SOLUTION = 4

fibo_max = 10 ** 10
fibo = [0, 1, 2]
while True:
    c = fibo[-2] + fibo[-1]
    if c > fibo_max:
        break
    fibo.append(c)


if SOLUTION == 0:

    # recherche basique dans le tableau de 50 éléments
    def is_fibo(n):
        return n in fibo

elif SOLUTION == 1:

    fibonacci = {}
    for i in fibo:
        fibonacci[i] = True

    # recherche par hash
    def is_fibo(n):
        return n in fibonacci

elif SOLUTION == 2:

    # binary search, fibo[] est déjà trié
    def is_fibo(n):
        i = bisect.bisect_right(fibo, n)
        return i > 0 and fibo[i - 1] == n

elif SOLUTION == 3:
    n_fibo = len(fibo)

    # autre dichotomie
    def is_fibo(n):
        i = bisect.bisect_left(fibo, n)
        return i < n_fibo and fibo[i] == n

elif SOLUTION == 4:
    n_fibo = len(fibo)

    # dichotomie manuelle
    def is_fibo(n):
        lo, hi = 0, n_fibo
        while lo < hi:
            mid = (lo + hi) // 2
            if fibo[mid] < n: lo = mid + 1
            elif fibo[mid] == n: return True
            else: hi = mid
        return False


for _ in range(int(input())):
    print("IsFibo" if is_fibo(int(input())) else "IsNotFibo")
