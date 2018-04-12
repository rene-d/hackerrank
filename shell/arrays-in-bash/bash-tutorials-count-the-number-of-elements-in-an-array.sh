# Linux Shell > Arrays in Bash > Count the number of elements in an Array
# Read in an Array - and count the number of elements in it.
#
# https://www.hackerrank.com/challenges/bash-tutorials-count-the-number-of-elements-in-an-array/problem
#

a=($(cat))
echo ${#a[@]}
