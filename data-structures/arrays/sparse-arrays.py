# Sparse Arrays
# Determine the number of times a string has previously appeared.
#
# https://www.hackerrank.com/challenges/sparse-arrays/problem
#

from collections import defaultdict

strings = defaultdict(lambda: 0)

for _ in range(int(input())):
    strings[input()] += 1

for _ in range(int(input())):
    print(strings[input()])
