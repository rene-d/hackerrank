# Regex > Assertions > Negative Lookbehind
# It asserts the regex to match if regexp behind is not matching.
#
# https://www.hackerrank.com/challenges/negative-lookbehind/problem
# challenge id: 14904
#

Regex_Pattern = r"(?<![aeiouAEIOU])."	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
