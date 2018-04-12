# Python > Built-Ins > Input()
# A Python 2 challenge: Input() is equivalent to eval(raw_input(prompt)).
#
# https://www.hackerrank.com/challenges/input/problem
#

x, y = map(int, input().split())
P = input()
print(y == eval(P, {'x':x}))
