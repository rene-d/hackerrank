# Regex > Introduction > Matching Anything But a Newline
# Use [.] in the regex expression to match anything but a newline character.
#
# https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem
# challenge id: 14095
#

regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
