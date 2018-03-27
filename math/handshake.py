# Handshake
# Count the number of Handshakes in a board meeting.
#
# https://www.hackerrank.com/challenges/handshake/problem
#

T = int(input())
for a0 in range(T):
    N = int(input())
    print(N * (N - 1) // 2)
