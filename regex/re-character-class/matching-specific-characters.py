# Regex > Character Class > Matching Specific Characters
# Use the [ ] expression to match specific characters.
#
# https://www.hackerrank.com/challenges/matching-specific-characters/problem
# challenge id: 14272
#

Regex_Pattern = r'^[123][012][xs0][30Aa][xsu][\.,]$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
