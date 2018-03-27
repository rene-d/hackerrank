# Cut the sticks
# Given the lengths of n sticks, print the number of sticks that are left before each cut operation.
#
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
#

def cutTheSticks(arr):
    # Complete this function

    # algorithme:
    # il faut soustraire la valeur minimale à chaque fois
    # et supprimer les éléments minimaux

    def iter():
        m = min(arr)
        for i in arr:
            if i > m:
                yield i - m

    while len(arr) > 0:
        print(len(arr))
        arr = list(iter())

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    cutTheSticks(arr)
