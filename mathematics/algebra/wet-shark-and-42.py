# Mathematics > Algebra > Wet Shark and 42
# Help Wet Shark escape the gods of 42.
#
# https://www.hackerrank.com/challenges/wet-shark-and-42/problem
# https://www.hackerrank.com/contests/infinitum9/challenges/wet-shark-and-42
#

def distance(n):
    return (n * 21 - 1) // 20 * 2

for _ in range(int(input())):
    n = int(input())
    print(distance(n) % 1000000007)
