# Interview Preparation Kit > Miscellaneous > Friend Circle Queries
# Process the queries and after each query print the number of people largest friend circle.
#
# https://www.hackerrank.com/challenges/friend-circle-queries/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=miscellaneous
# challenge id: 71478
#

from collections import defaultdict


def solve(L, R):
    ref = defaultdict(lambda: len(ref))
    members = [[] for i in range(200000)]
    groups = [0] * 200000
    m = 2                   # 2 is always the minimum group size
    k = 0

    for l, r in zip(L, R):

        l = ref[l]          # index (<200000) of person l
        r = ref[r]          # index of person r

        a = groups[l]       # group number of l
        b = groups[r]       # group number of r

        if a == 0 and b == 0:
            # new group
            k += 1
            groups[l] = k                       # l and r are belong to the same new group
            groups[r] = k
            members[k].append(l)
            members[k].append(r)

        elif a == 0:
            # a new friend in the group
            groups[l] = b
            members[b].append(l)                # l becomes friend with r' friends
            m = max(m, len(members[b]))         # update the max group size

        elif b == 0:
            # a new friend in the group
            groups[r] = a
            members[a].append(r)                # r becomes friend with l' ones
            m = max(m, len(members[a]))

        elif a == b:
            # already in the same group
            pass

        elif len(members[a]) > len(members[b]):
            # merge of 2 groups of friends
            members[a].extend(members[b])       # friends of r will be merged with l' ones
            for i in members[b]:
                groups[i] = a                   # update group number for the friends of l

            members[b] = None                   # we not longer need this group (it was merged)
            m = max(m, len(members[a]))

        else:
            # merge of 2 groups of friends
            members[b].extend(members[a])
            for i in members[a]:
                groups[i] = b

            members[a] = None
            m = max(m, len(members[b]))

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
