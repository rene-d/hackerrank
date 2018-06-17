# Regex > Introduction > Matching Whitespace & Non-Whitespace Character
# Use \s to match whitespace and \S to match non whitespace characters in this challenge.
#
# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem
# challenge id: 14233
#

Regex_Pattern = r"(\S\S\s){2}\S\S"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
