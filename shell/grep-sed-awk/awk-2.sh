# Linux Shell > Grep Sed Awk > 'Awk' - 2
# Let's play around with 'awk'.
#
# https://www.hackerrank.com/challenges/awk-2/problem
#

awk '{ if ($2 >= 50 && $3 >= 50 && $4 >= 50) print $1,": Pass"; else print $1, ": Fail" }'
