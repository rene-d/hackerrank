# Cats and a Mouse
#  Which cat will catch the mouse first?
#
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#

#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    #
    if abs(x - z) == abs(y - z):
        return "Mouse C"

    if abs(x - z) < abs(y - z):
        return "Cat A"

    return "Cat B"


if __name__ == '__main__':
    for _ in range(int(input())):
        x, y, z = map(int, input().split())
        print(catAndMouse(x, y, z))
