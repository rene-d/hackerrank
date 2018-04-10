# Mathematics > Fundamentals > Halloween party
# Help Alex give Silvia the maximum number of chocolates
#
# https://www.hackerrank.com/challenges/halloween-party/problem
#

for _ in range(int(input())):
    K = int(input())
    # K pair: on coupe K/2 fois horizontalement et K/2 fois verticalement
    # K impair: on coupe une fois de plus horizontalement ou verticalement
    print((K // 2) * ((K + 1) // 2))