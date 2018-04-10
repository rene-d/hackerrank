# Mathematics > Number Theory > Identify Smith Numbers
# Write a program to check whether a given integer is a Smith number.
#
# https://www.hackerrank.com/challenges/identify-smith-numbers/problem
#

def decompose(n):
    facteurs = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            facteurs.append(i)
        if i >= 3:
            i += 2
        else:
            i += 1
    if n > 1:
        facteurs.append(n)
    return facteurs


N = input()

# somme des chiffres des diviseurs
sd = sum(sum(map(int, list(str(d)))) for d in decompose(int(N)))

# somme des chiffres
sc = sum(map(int, list(N)))

print(int(sc == sd))
