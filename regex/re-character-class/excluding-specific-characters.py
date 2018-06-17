# Regex > Character Class > Excluding Specific Characters
# Use the [^] character class to exclude specific characters.
#
# https://www.hackerrank.com/challenges/excluding-specific-characters/problem
# challenge id: 14273
#

Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
