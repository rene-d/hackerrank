# Regex > Applications > UK and US: Part 2
# Use regular expression to count the number of occurrences of a given word with either *our* or *or* in it.
#
# https://www.hackerrank.com/challenges/uk-and-us-2/problem
# challenge id: 718
#

import re

words = (' '.join(input() for _ in range(int(input())))).lower().split()

for _ in range(int(input())):
    s = input().lower()

    us = re.sub(r'(\w+)(ou?r)(\w*)', r'\1or\3', s)
    uk = re.sub(r'(\w+)(ou?r)(\w*)', r'\1our\3', s)

    count = 0
    for w in words:
        if us == w or uk == w:
            count += 1
    print(count)
