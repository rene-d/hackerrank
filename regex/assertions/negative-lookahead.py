# Regex > Assertions > Negative Lookahead
# It asserts the regex to match if regexp ahead is not matching.
#
# https://www.hackerrank.com/challenges/negative-lookahead/problem
# challenge id: 14902
#

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
