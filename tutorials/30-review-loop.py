# Day 6: Let's Review
# Characters and Strings
#
# https://www.hackerrank.com/challenges/30-review-loop/problem
#

for _ in range(int(input())):
    s = input()
    # pas tout à fait le but du challenge, mais Python est élégant!
    print(s[::2], s[1::2])
