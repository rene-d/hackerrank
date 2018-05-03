# Python > Collections > Collections.namedtuple()
# You need to turn tuples into convenient containers using collections.namedtuple().
#
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#

from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input())
print(sum(int(Student(*(input().split())).MARKS) for _ in range(n)) / n)
