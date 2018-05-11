# 101 Hack June 2016 > Points On a Line
#  Given a set of coordinates, determine if they fall in an horizontal or vertical line.
#
# https://www.hackerrank.com/contests/101hack38/challenges/points-on-a-line
#

x0, y0 = 0, 0
same_x, same_y = True, True

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    if i == 0:
        x0, y0 = x, y
    else:
        same_x = same_x and x == x0
        same_y = same_y and y == y0

print("YES" if same_x or same_y else "NO")
