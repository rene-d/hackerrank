# Tutorials > 30 Days of Code > Day 28: RegEx, Patterns, and Intro to Databases
# Review Pattern documentation and start using Regular Expressions
#
# https://www.hackerrank.com/challenges/30-regex-patterns/problem
#

# où sont les regex ?...

gmail = {}

for _ in range(int(input())):
    firstName, emailID = input().split()
    if emailID.endswith("@gmail.com"):
        gmail[emailID] = firstName

for i in sorted(gmail.values()):
    print(i)
