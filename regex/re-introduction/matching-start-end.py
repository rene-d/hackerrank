# Regex > Introduction > Matching Start & End
# Use the ^ symbol to match the start of a string, and the $ symbol to match the end characters.
#
# https://www.hackerrank.com/challenges/matching-start-end/problem
# challenge id: 14268
#

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
