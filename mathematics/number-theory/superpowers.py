# Mathematics > Number Theory > Superpowers of 2
# Just another numbers problem...
#
# https://www.hackerrank.com/challenges/superpowers/problem
# https://www.hackerrank.com/contests/101hack20/challenges/superpowers
# challenge id: 5505
#

a, b = map(int, input().split())
print(pow(2, pow(2, a), b))
