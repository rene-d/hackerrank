# ACM ICPC Team
# Print the maximum topics a given team can cover for ACM ICPC World Finals
#
# https://www.hackerrank.com/challenges/acm-icpc-team/problem
#

import itertools


def acmTeam(topic):
    # Complete this function
    bt = [int(i, 2) for i in topic]

    def count_bits(i):
        return bin(i).count('1')
        # n = 0
        # while i != 0:
        #     i, r = divmod(i, 2)
        #     n += r
        # return n

    bmax = 0
    bmax_count = 0
    for i, j in itertools.combinations(bt, 2):
        b = count_bits(i | j)
        if b > bmax:
            bmax = b
            bmax_count = 1
        elif b == bmax:
            bmax_count += 1

    return bmax, bmax_count


if __name__ == "__main__":
    n, m = map(int, input().split())
    topic = []
    topic_i = 0
    for topic_i in range(n):
       topic_t = input().strip()
       topic.append(topic_t)
    result = acmTeam(topic)
    print ("\n".join(map(str, result)))
