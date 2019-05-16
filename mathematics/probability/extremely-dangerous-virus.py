# Mathematics > Probability > Extremely Dangerous Virus
# Estimate how large the virus will grow.
#
# https://www.hackerrank.com/challenges/extremely-dangerous-virus/problem
# https://www.hackerrank.com/contests/rookierank/challenges/extremely-dangerous-virus
# challenge id: 22940
#

a, b, t = map(int, input().split())

print(pow((a + b) // 2, t, 1000000007))
