# Linux Shell > Grep Sed Awk > 'Awk' - 4
# Let's play around with 'awk'.
#
# https://www.hackerrank.com/challenges/awk-4/problem
#

awk '{if (NR % 2) { printf $0 ";"; } else { printf $0 "\n"; } }'

# il y a moyen d'écrire beaucoup plus concis
