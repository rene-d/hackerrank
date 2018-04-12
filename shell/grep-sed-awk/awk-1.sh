# Linux Shell > Grep Sed Awk > 'Awk' - 1
# Introduction to the 'awk' command in Linux.
#
# https://www.hackerrank.com/challenges/awk-1/problem
#

awk '{ if (NF < 4) { print "Not all scores are available for "$1 }}'
