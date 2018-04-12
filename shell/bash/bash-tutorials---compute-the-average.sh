# Linux Shell > Bash > Compute the Average
# Compute the average of a list of N numbers provided to you.
#
# https://www.hackerrank.com/challenges/bash-tutorials---compute-the-average/problem
#

# pas franchement le langage le plus adapté...

export LANG=C

read N
a=0
for i in $(seq $N); do
    read x
    a=$((a+x))
done
printf "%.3f" $(bc -l <<< "$a / $N")
