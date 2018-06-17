# Mathematics > Number Theory > Help Mike
# Help Mike attend the NSA meeting
#
# https://www.hackerrank.com/challenges/help-mike/problem
# https://www.hackerrank.com/contests/sep13/challenges/help-mike
# challenge id: 803
#

for _ in range(int(input())):
    n, k = map(int, input().split())
    q, r = divmod(n, k)
    nb_pairs = k * (q - 1) * q // 2 + (r + (k - 1) // 2) * q
    if r > k // 2:
        nb_pairs += r - k // 2
    print(nb_pairs)
