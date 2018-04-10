# A Chocolate Fiesta
# Find the number of even subsets in the given set of numbers.
#
# https://www.hackerrank.com/challenges/a-chocolate-fiesta/problem
#

input()
a = list(map(int, input().split()))

n = len(a)
impairs = sum(1 for i in a if i % 2 == 1)

if impairs == 0:
    # nombre de combinaisons avec tous les nombres
    resultat = 2 ** n - 1
else:
    # il faut additionner un nombre pair de nombres impairs
    # i.e. considérer qu'on a un nombre impair de moins
    # c'est-à-dire un nombre en moins
    resultat = 2 ** (n - 1) - 1

print(resultat % 1000000007)
