# Insertion Sort - Part 2
# Code Insertion Sort itself.
#
# https://www.hackerrank.com/challenges/insertionsort2/problem
#

def insertionSort2(n, arr):

    for i in range(1, n):
        j = i
        while j > 0 and arr[i] < arr[j - 1]:
            j -= 1

        if j != i:
            e = arr[i]
            for k in range(i, j, -1):
                arr[k] = arr[k - 1]
            arr[j] = e

        print(' '.join(map(str, arr)))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
