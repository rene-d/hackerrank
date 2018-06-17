# Regex > Applications > HackerRank Tweets
# Write a regex to identify the tweets that has the string *hackerrank* in it
#
# https://www.hackerrank.com/challenges/hackerrank-tweets/problem
# https://www.hackerrank.com/contests/regex-practice-2/challenges/hackerrank-tweets
# challenge id: 714
#

import re

n = 0
for _ in range(int(input())):
    if re.search(r'\bhackerrank\b', input(), re.I):
        n += 1
print(n)
