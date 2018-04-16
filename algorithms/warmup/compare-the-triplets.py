# Algorithms > Warmup > Compare the Triplets
# Compare the elements in two triplets.
# 
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# 

a = map(int, input().split())
b = map(int, input().split())
alice, bob = 0, 0
for i, j in zip(a, b):
    if i > j:
        alice += 1
    elif i < j:
        bob += 1
print(alice, bob)
