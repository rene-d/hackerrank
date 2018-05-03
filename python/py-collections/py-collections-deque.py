# Python > Collections > Collections.deque()
# Perform multiple operations on a double-ended queue or deque.
#
# https://www.hackerrank.com/challenges/py-collections-deque/problem
#

from collections import deque

d = deque()

for _ in range(int(input())):
    cmd, _, opt = input().strip().partition(' ')
    if cmd == "append":
        d.append(opt)
    elif cmd == "appendleft":
        d.appendleft(opt)
    elif cmd == "pop":
        d.pop()
    elif cmd == "popleft":
        d.popleft()

print(" ".join(d))
