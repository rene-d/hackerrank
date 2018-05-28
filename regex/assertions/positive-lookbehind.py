# Regex > Assertions > Positive Lookbehind
# It asserts the regex to match if regexp behind is matching.
#
# https://www.hackerrank.com/challenges/positive-lookbehind/problem
# challenge id: 14903
#

Regex_Pattern = r"(?<=[13579])\d"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
