# Exceptions
# Handle errors detected during execution.
# 
# https://www.hackerrank.com/challenges/exceptions/problem
# 

n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        a = int(a)
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(a))
        continue
    try:
        b = int(b)
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(b))
        continue
    try:
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
        continue
