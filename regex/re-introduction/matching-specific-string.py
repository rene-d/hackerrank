# Regex > Introduction > Matching Specific String
# Match a specific string using regex.
#
# https://www.hackerrank.com/challenges/matching-specific-string/problem
# https://www.hackerrank.com/contests/regular-expresso/challenges/matching-specific-string
# challenge id: 13619
#

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
