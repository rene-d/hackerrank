# Mathematics > Algebra > Triangle Numbers
# Given a triangle numbers where each number is equal to the sum of the three top numbers, find the first even number in a row.
#
# https://www.hackerrank.com/challenges/triangle-numbers/problem
#


def v(row, col):
   # print("v", row, col)

    if abs(col) == row:
        return 1
    elif abs(col) > row:
        return 0
    else:
        return v(row - 1, col) + v(row-1, col - 1) + v(row-1, col + 1)


def test():
    N = 14
    for n in range(1, N):
        s = "      " * (N - n)
        for i in range(-n , n + 1):
            x = v(n, i)
            s += "{:5d} ".format(x)
            #if x % 2 == 0: break
        print("{:4} {}".format(n + 1, s[:100]))


for _ in range(int(input())):
    n = int(input())
    if n <= 2:
        print(-1)       # pas de pair dans les deux premières rangées
    elif n % 2 == 1:
        print(2)        # rangée impaire: position 2
    elif n % 4 == 0:
        print(3)        # rangée doublement paire: position 3
    else:
        print(4)        # rangée simplement paire: position 4
