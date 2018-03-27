# Summing the N series 
# Sum the N series.
# 
# https://www.hackerrank.com/challenges/summing-the-n-series/problem
# 

# c'est quand même plus facile que les problèmes de Project Euler...

for _ in range(int(input())):
    n = int(input())
    print((n ** 2) % 1000000007)

