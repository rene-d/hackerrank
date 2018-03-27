# Save the Prisoner!
# Given M sweets and a circular queue of N prisoners, find the ID of the last prisoner to receive a sweet.
#
# https://www.hackerrank.com/challenges/save-the-prisoner/problem
#

def saveThePrisoner(n, m, s):
    # Complete this function
    # le résultat est l'addition du numéro du prisionnier et du nombre
    # de bonbons modulo le nombre de prisonniers. -1 parce qu'il faut
    # compter en partant de 0, et +1 parce que les numéros commencent à 1
    return 1 + (s - 1 + m - 1) % n


t = int(input())
for a0 in range(t):
    n, m, s = map(int, input().split())
    result = saveThePrisoner(n, m, s)
    print(result)
