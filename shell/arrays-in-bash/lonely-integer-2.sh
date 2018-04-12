# Linux Shell > Arrays in Bash > Lonely Integer - Bash!
# Find the integer that occurs only once in the Array
#
# https://www.hackerrank.com/challenges/lonely-integer-2/problem
#

# il suffit de faire des XOR avec les nombres
# les nombres en double vont s'annuler
# le nombre isolé va rester

read n
a=($(cat))
echo $((0 ${a[@]/#/^}))
