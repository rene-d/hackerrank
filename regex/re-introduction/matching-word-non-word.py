# Regex > Introduction > Matching Word & Non-Word Character
# Use \w to match any word and \W to match any non-word character.
#
# https://www.hackerrank.com/challenges/matching-word-non-word/problem
# challenge id: 14140
#

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
