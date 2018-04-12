# Linux Shell > Bash > Arithmetic Operations
# Math in shell scripts.
#
# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
#

# mais ce n'est certainement pas la solution attendue...
#python3 -c 'print("%.3f" % eval(input().replace("^","**")))'

# c'est plus vraisemblalement ça... dommage que scale=3 ne donne pas les bonnes décimales
export LANG=C
read a
printf "%.3f\n" $(echo $a | bc -l)
