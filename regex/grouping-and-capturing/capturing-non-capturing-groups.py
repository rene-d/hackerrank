# Regex > Grouping and Capturing > Capturing & Non-Capturing Groups
# Creating capturing and non-capturing group.
#
# https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem
# challenge id: 14621
#

Regex_Pattern = r'(?:ok){3,}'	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
