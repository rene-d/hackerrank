# Linux Shell > Arrays in Bash > Filter an Array with Patterns
# Read in an array and filter out certain elements based on a pattern.
#
# https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns/problem
#

declare -a a

a=($(cat))

echo ${a[@]/*[aA]*/}
