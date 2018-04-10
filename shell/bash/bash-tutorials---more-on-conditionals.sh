# Linux Shell > Bash > More on Conditionals
# Three sides of a triangle are provided to you. Is the Triangle Scalene, Equilateral or Isosceles?
#
# https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem
#

read X
read Y
read Z
if [ $X -eq $Y -a $Y -eq $Z -a $Z -eq $X ] ; then
    echo EQUILATERAL
elif [ $X -eq $Y -o $Y -eq $Z -o $Z -eq $X ] ; then
    echo ISOSCELES
else
    echo SCALENE
fi
