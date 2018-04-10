# QHEAP1
# Solve the basic heap question with insertion and deletion.
#
# https://www.hackerrank.com/challenges/qheap1/problem
#
from heapq import heappush, heapify, heappop

q = []
q2 = []

for _ in range(int(input())):
    op = list(map(int, input().split()))

    # add
    if op[0] == 1:
        heappush(q, op[1])

    # del
    elif op[0] == 2:
        #q.remove(op[1])
        #heapify(q)
        heappush(q2, op[1])

    # print
    elif op[0] == 3:
        #print(q[0])
        while len(q2) > 0 and q[0] == q2[0]:
            heappop(q)
            heappop(q2)
        print(q[0])
