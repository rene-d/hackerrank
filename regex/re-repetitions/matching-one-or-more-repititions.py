# Regex > Repetitions > Matching One Or More Repetitions
# Match zero or more repetitions of character/character class/group with the + symbol.
#
# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem
# challenge id: 14524
#

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
