# Tutorials > 30 Days of Code > Day 9: Recursion
# Use recursion to compute the factorial of number.
#
# https://www.hackerrank.com/challenges/30-recursion/problem
#

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
