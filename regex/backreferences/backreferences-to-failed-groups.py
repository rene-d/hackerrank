# Regex > Backreferences > Backreferences To Failed Groups
# Backreference to a capturing group that match nothing.
#
# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem
# challenge id: 14743
#

Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
