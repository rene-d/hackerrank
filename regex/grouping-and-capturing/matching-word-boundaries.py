# Regex > Grouping and Capturing > Matching Word Boundaries
# Using \b to match word boundaries.
#
# https://www.hackerrank.com/challenges/matching-word-boundaries/problem
# challenge id: 14619
#

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
