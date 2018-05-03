# Python > Collections > Company Logo
# Print the number of character occurrences in descending order.
#
# https://www.hackerrank.com/challenges/most-commons/problem
#

from collections import Counter
from itertools import groupby

name = input()

nb = 0
for c, g in groupby(Counter(name).most_common(), key=lambda x: x[1]):
    for l in sorted(map(lambda x: x[0], g)):
        print(l, c)
        nb += 1
        if nb == 3: break
    if nb == 3: break
