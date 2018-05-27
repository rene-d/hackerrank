# Regex > Repetitions > Matching {x, y} Repetitions
# Match between a range of x and y repetitions using the {x,y} tool.
#
# https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem
# challenge id: 14522
#

Regex_Pattern = r'^\d{1,2}[A-Za-z]{3,}\.{0,3}$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
