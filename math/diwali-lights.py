# Diwali Lights
# Number of ways to light the room
#
# https://www.hackerrank.com/challenges/diwali-lights/problem
#

# chaque lampe peut être allumée ou éteinte
# il y a donc 2^n possibilités pour n lampes
# -1 parce qu'il en faut une allumé

for n in range(int(input())):
    n = int(input())
    print((2 ** n  - 1) % 100000)