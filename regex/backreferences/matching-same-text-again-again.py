# Regex > Backreferences > Matching Same Text Again & Again
# Match the same text as previously matched by the capturing group.
#
# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem
# https://www.hackerrank.com/contests/regular-expresso/challenges/matching-same-text-again-again
# challenge id: 14740
#

Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
