# Python > Built-Ins > Any or All
# Return True, if any of the iterable is true or if all of it is true using the any() and all() expressions.
#
# https://www.hackerrank.com/challenges/any-or-all/problem
#

_, arr = input(), list(map(int, input().split()))
print(all(i >= 0 for i in arr) and any((i < 10 or i % 11 == 0) for i in arr))
