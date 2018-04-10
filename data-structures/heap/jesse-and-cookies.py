# Jesse and Cookies
# Calculate the number of operations needed to increase the sweetness of the cookies so that each cookie in the collection has a sweetness >=K.
#
# https://www.hackerrank.com/challenges/jesse-and-cookies/problem
#

import heapq


def cookies(k, A):

    stack = sorted(A)
    heapq.heapify(stack)

    op = 0
    while stack[0] < k and len(stack) >= 2:
        a = heapq.heappop(stack)
        a = a + 2 * heapq.heappop(stack)
        heapq.heappush(stack, a)
        op += 1

    if stack[0] < k: return -1
    return op


if __name__ == '__main__':
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    op = cookies(k, A)
    print(op)
