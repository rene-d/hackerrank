# Regex > Applications > The British and American Style of Spelling
# Use regular expression to find the count of a given word that ends with either *ze* or *se*
#
# https://www.hackerrank.com/challenges/uk-and-us/problem
# challenge id: 710
#

import re

text = ''
for _ in range(int(input())):
    text += input() + ' '

for _ in range(int(input())):
    w = input()
    print(len(re.findall(w[:len(w) - 2] + r'[sz]e\b', text)))
