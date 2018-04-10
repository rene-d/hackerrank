# Linux Shell > Bash > Comparing Numbers
# Simple comparisons between numbers: Greater than, less than, equal to.
#
# https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem
#

read X
read Y
[ $X -eq $Y ] && echo "X is equal to Y"
[ $X -lt $Y ] && echo "X is less than Y"
[ $X -gt $Y ] && echo "X is greater than Y"
