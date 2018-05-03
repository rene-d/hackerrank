# Python > Python Functionals > Map and Lambda Function
# This challenge covers the basic concept of maps and lambda expressions.
#
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
#

cube = lambda x: x ** 3

def fibonacci(n):
    """ return a list of fibonacci numbers """
    fibo = [0, 1]
    while len(fibo) < n:
        c = fibo[-2] + fibo[-1]
        fibo.append(c)
    return fibo[0:n]


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
