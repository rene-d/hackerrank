# Mathematics > Combinatorics > Sherlock and Pairs
# Count the number of pairs that satisfy a given constraint.
#
# https://www.hackerrank.com/challenges/sherlock-and-pairs/problem
# https://www.hackerrank.com/contests/101feb14/challenges/sherlock-and-pairs
# challenge id: 1932
#

for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))

    s = {}
    for i in a:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1

    print(sum(i * (i - 1) for i in s.values()))
