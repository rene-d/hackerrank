# Python > Math > Triangle Quest 2
# Create a palindromic triangle.
#
# https://www.hackerrank.com/challenges/triangle-quest-2/problem
#


# (template_tail) ----------------------------------------------------------------------
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(123456789 // (10 ** (9-i)) * (10 ** (i - 1)) + 987654321 % (10 ** (i - 1)))
