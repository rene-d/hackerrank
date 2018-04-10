# Linux Shell > Bash > Getting started with conditionals
# -
#
# https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem
#

read c
if [ "$c" = "y" -o "$c" = "Y" ]
then
    echo YES
else
    echo NO
fi
