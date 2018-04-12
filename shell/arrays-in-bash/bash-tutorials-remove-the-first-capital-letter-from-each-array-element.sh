# Linux Shell > Arrays in Bash > Remove the First Capital Letter from Each Element
# The first capital letter in each element should be replaced with a dot ('.').
#
# https://www.hackerrank.com/challenges/bash-tutorials-remove-the-first-capital-letter-from-each-array-element/problem
#

a=($(cat))
echo ${a[@]/#?/.}
