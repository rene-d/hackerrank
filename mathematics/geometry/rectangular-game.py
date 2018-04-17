# Mathematics > Geometry > Rectangular Game
# What's the largest number in the rectangular grid?
#
# https://www.hackerrank.com/challenges/rectangular-game/problem
#

# sans forcer, la réponse est clairement min(x) * min(y)

n = int(input())
mx, my = map(int, input().split())
for _ in range(n - 1):
    x, y = map(int, input().split())
    mx = min(x, mx)
    my = min(y, my)
print(mx * my)
