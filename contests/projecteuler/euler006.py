# ProjectEuler+ > Project Euler #6: Sum square difference
# Difference between sum of squares and square of sums.
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006
# challenge id: 2632
#

for _ in range(int(input())):
    n = int(input())

    # (Σ𝑖)² = 𝑛² * (𝑛+1)² * 1/4
    # Σ(𝑖²) = 𝑛 * (𝑛+1) * (2𝑛+1) * 1/6

    sq_sum = n ** 2 * (n + 1) ** 2 // 4
    sum_sq = n * (n + 1) * (2 * n + 1) // 6

    print(sq_sum - sum_sq)

    # autre possibilité (calcul avec Mathematica)
    # = 1/12 𝑛 (𝑛+1) (3𝑛+2) (𝑛-1)
