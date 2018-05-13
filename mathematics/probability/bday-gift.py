# Mathematics > Probability > B'day Gift
# Whats the price Isaac has to pay for HackerPhone
#
# https://www.hackerrank.com/challenges/bday-gift/problem
# https://www.hackerrank.com/contests/nov13/challenges/bday-gift
#

# chaque boule a une probabilité 0.5 d'être ramassée

n = int(input())
e = sum(int(input()) for _ in range(n))
print(e / 2)
