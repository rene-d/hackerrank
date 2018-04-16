# Tutorials > 30 Days of Code > Day 16: Exceptions - String to Integer
# Can you determine if a string can be converted to an integer?
#
# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
#

S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
