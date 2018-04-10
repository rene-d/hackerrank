# Gemstones
# Find the number of different gem-elements present.
#
# https://www.hackerrank.com/challenges/gem-stones/problem
#

# les minéraux de chaque pierre
minerals = [set(input()) for _ in range(int(input()))]

# minéraux présents dans toutes les pierres
minerals = set.intersection(*minerals)

# le résultat...
print(len(minerals))
