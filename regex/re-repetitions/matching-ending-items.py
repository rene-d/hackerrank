# Regex > Repetitions > Matching Ending Items
# Match the end of the string using the $ boundary matcher.
#
# https://www.hackerrank.com/challenges/matching-ending-items/problem
# challenge id: 14620
#

Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
