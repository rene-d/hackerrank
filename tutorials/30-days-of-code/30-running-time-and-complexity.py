# Tutorials > 30 Days of Code > Day 25: Running Time and Complexity
# Determine if a number is prime in optimal time!
#
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
#


def est_premier(n):
    """ teste si le nombre est premier """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 2
        return True


for _ in range(int(input())):
    print("Prime" if est_premier(int(input())) else "Not prime")
