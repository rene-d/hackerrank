# Bon Appétit
# Determine whether or not Brian overcharged Anna for their split bill.
# 
# https://www.hackerrank.com/challenges/bon-appetit/problem
# 

n, k = map(int, input().split())
b = list(map(int, input().split()))
p = int(input())

cc = sum(v for i, v in enumerate(b) if i != k)
brian = cc / 2 + b[k - 1]
anna = cc / 2

if p == anna:
    print('Bon Appetit')
else:
    print(round(p - anna))
