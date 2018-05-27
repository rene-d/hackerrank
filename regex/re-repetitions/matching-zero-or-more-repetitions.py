# Regex > Repetitions > Matching Zero Or More Repetitions
# Match zero or more repetitions of character/character class/group using the * symbol in regex.
#
# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions/problem
# challenge id: 14523
#

Regex_Pattern = r'^\d\d\d*[a-z]*[A-Z]*$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
