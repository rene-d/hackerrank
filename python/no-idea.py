"""
No Idea!

https://www.hackerrank.com/challenges/no-idea/problem
"""

input()

N = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

h = 0
for n in N:
    if n in A: h += 1
    if n in B: h -= 1
print(h)
