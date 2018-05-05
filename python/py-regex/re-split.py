# Python > Regex and Parsing > Re.split()
# Split the string by the pattern occurrence using the re.split() expression.
#
# https://www.hackerrank.com/challenges/re-split/problem
#

regex_pattern = r"[,.]"	# Do not delete 'r'.

# (skeliton_tail) ----------------------------------------------------------------------
import re
print("\n".join(re.split(regex_pattern, input())))
