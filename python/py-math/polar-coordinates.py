# Python > Math > Polar Coordinates
# Convert complex numbers to polar coordinates
#
# https://www.hackerrank.com/challenges/polar-coordinates/problem
#

import cmath

c = complex(input())

print(abs(c))               # 𝑟
print(cmath.phase(c))       # φ
