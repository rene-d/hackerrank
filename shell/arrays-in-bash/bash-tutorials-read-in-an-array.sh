# Linux Shell > Arrays in Bash > Read in an Array
# Read in an Array - and display all its elements.
#
# https://www.hackerrank.com/challenges/bash-tutorials-read-in-an-array/problem
#

a=($(cat))
echo ${a[@]}
