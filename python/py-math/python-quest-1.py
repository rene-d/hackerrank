# Python > Math > Triangle Quest
# Print a numeric triangle of height N-1 using only 2 lines.
#
# https://www.hackerrank.com/challenges/python-quest-1/problem
#

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * (10 ** i // 9))
