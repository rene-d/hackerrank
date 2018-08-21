# Mathematics > Number Theory > Sherlock Puzzle
# Help Sherlock get close to his Arch Nemesis, Jim Moriarty.
#
# https://www.hackerrank.com/challenges/sherlock-puzzle/problem
# https://www.hackerrank.com/contests/sep13/challenges/sherlock-puzzle
# challenge id: 836
#

from bisect import bisect_left

K, S = input().split()
K = int(K)
n = len(S)

s = [0] * (n + 1)
a = [0] * (n + 1)
a[0] = (0, 0)
for i in range(n):
    s[i + 1] = s[i] - 3 * (S[i] == '1') + 2 * (S[i] == '0')
    a[i + 1] = (s[i + 1], i + 1)

a.sort()
dp = [0] * (n + 1)
dp[0] = a[0][1]
for i in range(n):
    dp[i + 1] = max(dp[i], a[i + 1][1])

answer = 0
for i in range(n):
    dx = a[0][0] - s[i]
    if s[n] <= 0:
        x = K - 1
        if dx + s[n] * x > 0:
            continue
    elif dx > 0:
        continue
    else:
        x = min(K - 1, -dx // s[n])

    v = x * s[n] - s[i]
    p = bisect_left(a, (-v + 1, 0)) - 1
    answer = max(answer, dp[p] - i + x * n)

print(answer)
