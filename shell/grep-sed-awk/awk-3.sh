# Linux Shell > Grep Sed Awk > 'Awk' - 3
# Let's play around with 'awk'.
#
# https://www.hackerrank.com/challenges/awk-3/problem
#
awk '{ p = int(($2 + $3 + $4) / 3);
       if (p >= 80) q = "A"; else if (p >= 60) q = "B"; else if (p >= 50) q = "C"; else  q ="FAIL";
       print $1" "$2" " $3" " $4 " : " q ; }'
