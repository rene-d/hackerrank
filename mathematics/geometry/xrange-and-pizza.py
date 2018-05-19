# Mathematics > Geometry > Xrange's Pancakes
# Determine who needs to be added to the end of the line to restore the pancake to its initial orientation.
#
# https://www.hackerrank.com/challenges/xrange-and-pizza/problem
# https://www.hackerrank.com/contests/infinitum16/challenges/xrange-and-pizza
# challenge id: 12799
#


n, m = map(int, input().split())
a = 0               # position du pancake
flip = False        # est-ce qu'on l'a retourné?
for _ in range(m):
    op, k = map(int, input().split())
    if op == 1:
        a = (a + k) % n         # rotation de k
    else:
        a = (n - a + k) % n     # flip et rotation de k
        flip = not flip
if flip:
    print(2, a)
else:
    print(1, (n - a) % n)
