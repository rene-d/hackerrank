# Regex > Character Class > Matching Character Ranges
# Write a RegEx matching a range of characters.
#
# https://www.hackerrank.com/challenges/matching-range-of-characters/problem
# challenge id: 14274
#

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
