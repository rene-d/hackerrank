# Regex > Introduction > Matching Digits & Non-Digit Characters
# Use the expression \d to match digits and \D to match non-digit characters.
#
# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
# challenge id: 14186
#

Regex_Pattern = r"(\d\d\D){2}\d{4}"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
