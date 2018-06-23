# https://www.hackerrank.com/challenges/friend-circle-queries/problem


from collections import defaultdict


def solve(L, R):
    sizes = [[] for i in range(200000)]
    groups = [0] * 200000
    m = 2
    ref = defaultdict(lambda : len(ref))
    k = 0

    for l, r in zip(L, R):

        l = ref[l]
        r = ref[r]

        a = groups[l]
        b = groups[r]

        if a == 0 and b == 0:
            # new group
            k += 1
            groups[l] = k
            groups[r] = k
            sizes[k].append(l)
            sizes[k].append(r)

        elif a == 0:
            # a new friend in the group
            groups[l] = b
            sizes[b].append(l)
            m = max(m, len(sizes[b]))

        elif b == 0:
            # a new friend in the group
            groups[r] = a
            sizes[a].append(r)
            m = max(m, len(sizes[a]))

        elif a > b:
            # fusion of 2 groups
            sizes[a].extend(sizes[b])
            for i in sizes[b]:
                groups[i] = a

            sizes[b] = None
            m = max(m, len(sizes[a]))

        elif a < b:
            # fusion of 2 groups
            sizes[b].extend(sizes[a])
            for i in sizes[a]:
                groups[i] = b

            sizes[a] = None
            m = max(m, len(sizes[b]))

        else:
            # already in the same group
            pass

        print(m)


q = int(input())
L = list(map(int, input().rstrip().split()))
R = list(map(int, input().rstrip().split()))
solve(L, R)



""" trivial and Time Limit Exceed solution

def solve(L, R):
    groups = {}
    m = 0

    for l, r in zip(L, R):

        u = set([l, r])

        if l in groups: u |= groups[l]
        if r in groups: u |= groups[r]

        for i in u:
            groups[i] = u

        l = len(u)
        if m < l: m = l
        print(m)

"""
