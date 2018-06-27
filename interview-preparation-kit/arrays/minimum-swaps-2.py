# Interview Preparation Kit > Arrays > Minimum Swaps 2
# Return the minimum number of swaps to sort the given array.
#
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=arrays
# challenge id: 70816
#

def minimumSwaps(q):
    q.insert(0, 0)
    length = len(q)

    # minimal swaps:
    ref = [0] * length
    for i, x in enumerate(q):
        ref[x] = i

    swaps = 0
    for i in range(length):
        k = q[i]
        if k != i:
            q[i], q[ref[i]] = q[ref[i]], q[i]
            ref[i], ref[k] = ref[k], ref[i]
            swaps += 1

    print(swaps)


n = int(input())
arr = list(map(int, input().split()))
minimumSwaps(arr)
