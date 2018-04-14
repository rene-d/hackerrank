# Tutorials > 30 Days of Code > Day 27: Testing
# Welcome to Day 27! Review testing in this challenge!
#
# https://www.hackerrank.com/challenges/30-testing/problem
#

from random import randint

print(5)

# YES (cancelled, il faut au plus k-1 nombres <= 0)
def yes():
    n = randint(50, 200)
    k = randint(10, n - 5)
    print(n, k)
    A = [0]
    for i in range(k - 2):
        A.append(randint(-1000, -1))
    while len(A) < n:
        A.append(randint(1, 1000))
    print(' '.join(map(str, A)))

# NO (il faut au moins k nombres <= 0)
def no():
    n = randint(50, 200)
    k = randint(10, n - 5)
    print(n, k)
    A = [0]
    for i in range(k + 2):
        A.append(randint(-1000, -1))
    while len(A) < n:
        A.append(randint(1, 1000))
    print(' '.join(map(str, A)))

yes()
no()
yes()
no()
yes()
