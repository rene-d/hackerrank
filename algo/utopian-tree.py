# Utopian Tree
# Predict the height of the tree after N growth cycles.
#
# https://www.hackerrank.com/challenges/utopian-tree/problem
#


def utopianTree(n):
    # Complete this function
    H = 1
    for i in range(n):
        if i % 2 == 0:
            H *= 2
        else:
            H += 1
    return H


if __name__ == "__main__":
    t = int(input())
    for a0 in range(t):
        n = int(input())
        result = utopianTree(n)
        print(result)
