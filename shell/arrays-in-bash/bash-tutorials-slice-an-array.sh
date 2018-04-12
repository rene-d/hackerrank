# Linux Shell > Arrays in Bash > Slice an Array
# Slice a given array.
#
# https://www.hackerrank.com/challenges/bash-tutorials-slice-an-array/problem
#

declare -a a

a=($(cat))
echo ${a[*]:3:5}
