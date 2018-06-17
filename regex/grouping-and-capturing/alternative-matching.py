# Regex > Grouping and Capturing > Alternative Matching
# Matching single regex out of several regex.
#
# https://www.hackerrank.com/challenges/alternative-matching/problem
# challenge id: 14623
#

Regex_Pattern = r'^(Mr|Ms|Mrs|Dr|Er)\.[a-zA-Z]+$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
