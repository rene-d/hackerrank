# Jumping on the Clouds
# Jumping on the clouds
#
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
#

# il faut raisonner en partant de la fin et en essayant
# de faire des bonds 2 autant que possibe


ORDINARY_CLOUD = 0
THUNDER_CLOUD = 1


def jumpingOnClouds(c):
    i = len(c) - 1
    jumps = 0
    while i > 0:
        jumps += 1
        if i >- 2 and c[i - 2] == ORDINARY_CLOUD:
            i -= 2
        else:
            assert c[i - 1] == ORDINARY_CLOUD
            i -= 1
    return jumps


if __name__ == "__main__":
    input()
    c = list(map(int, input().split()))
    result = jumpingOnClouds(c)
    print(result)
