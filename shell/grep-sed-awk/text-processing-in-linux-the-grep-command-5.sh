# Linux Shell > Grep Sed Awk > 'Grep' - B
# Let's 'grep' out stuff from text files!
#
# https://www.hackerrank.com/challenges/text-processing-in-linux-the-grep-command-5/problem
#

grep -E '([0-9]) ?\1'

# -E extended grep
# ([0-9]) = capture un chiffre
# " ?" = un espace ou rien
# \1 = référence à la capture
