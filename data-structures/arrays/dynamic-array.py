# Dynamic Array
# Learn to use dynamic arrays by solving this problem.
#
# https://www.hackerrank.com/challenges/dynamic-array/problem
#


def dynamicArray(n, queries):

    last_answer = 0
    seq = [[] for _ in range(n)]

    for q in queries:
        op, x, y = q

        if op == 1:
            seq[(x ^ last_answer) % n].append(y)
        elif op == 2:
            s = seq[(x ^ last_answer) % n]
            last_answer = s[y % len(s)]
            print(last_answer)


if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))

    dynamicArray(n, queries)
