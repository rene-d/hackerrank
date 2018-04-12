# Python > Built-Ins > Zipped!
# Compute the average by zipping data.
#
# https://www.hackerrank.com/challenges/zipped/problem
#

n, x = map(int, input().split())
a = []
for _ in range(x):
    a.append(list( map(float, input().split())))
for i in zip(*a):
    print(sum(i) / x)