# Special Multiple
# Can you find the least positive integer that is made of only 0s and 9s? - 30 Points
#
# https://www.hackerrank.com/challenges/special-multiple/problem
#

# Le plus simple est décrire 1, 2, 3... en "binaire" {0,9} (au lieu de {0,1})
# et tester la divisibilité du nombre trouvé

# Amusant :) L'éditorial donne la même solution élégante en Python
# tandis que le tester code est carrément plus obscur

def nine_zero(n):
    for i in range(1, 100000):
        f = int(bin(i)[2:]) * 9
        if f % n == 0:
            return f
    return "?"


for n in range(int(input())):
    print(nine_zero(int(input())))