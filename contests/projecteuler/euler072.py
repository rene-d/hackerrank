# ProjectEuler+ > Project Euler #72: Counting fractions
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler072
# challenge id: 2698
#


def totients(n):
    """ retourne la liste des indicatrices d'Euler (ou totient) pour 2 <= i <= n """
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:     # i est premier
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi[2:]          # supprime 0 et 1


# précalcule tous les résultats possibles
MAX = 1000000
results = [0] * (MAX + 1)
for i, phi in enumerate(totients(MAX), 2):
    results[i] = results[i - 1] + phi

for _ in range(int(input())):
    n = int(input())
    print(results[n])
