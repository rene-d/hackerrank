# Linux Shell > Arrays in Bash > Display an element of an array
# Read in an Array - and display the fourth element in it.
#
# https://www.hackerrank.com/challenges/bash-tutorials-display-the-third-element-of-an-array/problem
#

a=($(cat))
echo ${a[3]}