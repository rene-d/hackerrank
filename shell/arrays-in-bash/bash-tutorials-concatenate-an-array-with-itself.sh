# Linux Shell > Arrays in Bash > Concatenate an array with itself
# Concatenate an array with itself.
#
# https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself/problem
#

declare -a a
a=($(cat))
b=("${a[@]}" "${a[@]}" "${a[@]}")
echo ${b[@]}
