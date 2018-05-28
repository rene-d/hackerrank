# Regex > Assertions > Positive Lookahead
# A positive lookahead asserts the regex to match if the regexp ahead is matching.
#
# https://www.hackerrank.com/challenges/positive-lookahead/problem
# https://www.hackerrank.com/contests/regular-expresso/challenges/positive-lookahead
# challenge id: 14901
#

Regex_Pattern = r'o(?=oo)'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
