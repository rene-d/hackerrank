# Russian Peasant Exponentiation
# The only correct way to raise numbers in powers.
#
# https://www.hackerrank.com/challenges/russian-peasant-exponentiation/problem
#

for _ in range(int(input())):
    a, b, k, m = map(int, input().split())

    # calcule (a + b∙𝑖)^k mod m

    if k == 0:
        print(1, 0)
    else:
        while k % 2 == 0:
            # (a + b∙𝑖)² = a² + 2a∙b∙𝑖 - b²
            a, b = a * a - b * b, 2 * a * b
            a, b = a % m, b % m
            k //= 2

        c, d = a, b
        k //= 2

        while k > 0:
            a, b = a * a - b * b, 2 * a * b
            a, b = a % m, b % m

            if k % 2 == 1:
                # (a + b∙𝑖)×(c + d∙𝑖)
                c, d = a * c - b * d, d * a + c * b
                c, d = c % m, d % m

            k //= 2

        print(c, d)
