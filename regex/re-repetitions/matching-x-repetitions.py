# Regex > Repetitions > Matching {x} Repetitions
# Match exactly x repetitions using the tool {x}.
#
# https://www.hackerrank.com/challenges/matching-x-repetitions/problem
# challenge id: 14525
#

Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
