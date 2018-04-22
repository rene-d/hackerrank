# Mathematics > Fundamentals > Possible Path
# Help Adam in reaching at aa particular point.
#
# https://www.hackerrank.com/challenges/possible-path/problem
#

from math import gcd

for _ in range(int(input())):
    a, b, x, y = map(int, input().split())

    print(["NO", "YES"][gcd(a, b) == gcd(x, y)])

    # il faut bien comprendre le phrasé de l'énoncé...
    # (a,b) change à chaque déplacement
    # print(["NO", "YES"][(x - a) % b == 0 and (y - b) % a == 0])
