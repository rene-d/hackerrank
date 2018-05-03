# Python > Collections > collections.Counter()
# Use a counter to sum the amount of money earned by the shoe shop owner. 
# 
# https://www.hackerrank.com/challenges/collections-counter/problem
# 

from collections import Counter

input()
shoes = Counter(input().split())
earned = 0
for _ in range(int(input())):
    shoe, price = input().split()
    if shoes[shoe]:
        shoes[shoe] -= 1
        earned += int(price)
print(earned)
