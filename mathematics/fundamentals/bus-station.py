# Mathematics > Fundamentals > Bus Station
# Find all suitable bus sizes
#
# https://www.hackerrank.com/challenges/bus-station/problem
#

#TODO
import sys

n = int(input())
a = list(map(int, input().split()))
result = []

# solution timeout
if False:
    max = sum(a)
    bus = 1
    while bus <= max:
        if max % bus != 0:
            bus += 1
            continue

        x = bus
        i = 0
        while i < n:
            x -= a[i]
            if x < 0: break
            if x == 0:
                x = bus
            i += 1
        if i == n and x == bus:
            # sys.stdout.write(str(bus) + " ")
            result.append(str(bus))

        bus += 1

# solution OK
# on considère la taille du bus R comme le cumul des groupes qui restent
# et on vérifie que les groupes précédents sont compatibles
# |------------------------------------|
#  <----- L -----><-------- R -------->
# à chaque instant, on doit avoir les groupes du côté L qui tiennent
# parfaitement dans un bus de taille R
if True:
    L = 0
    R = sum(a)

    for x in a:
        if R == 0:
            break

        if L % R == 0:
            bus = 0
            for i in a:
                bus += i
                if bus == R:
                    bus = 0
                elif bus > R:
                    break
            if bus == 0:
                result.insert(0, str(R))

        L += x
        R -= x

print(" ".join(result))
