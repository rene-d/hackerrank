# Insertion Sort - Part 1
# Insert an element into a sorted array.
#
# https://www.hackerrank.com/challenges/insertionsort1/problem
#

def insertionSort1(n, arr):
    # Complete this function
    e = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < e:
            arr[i + 1] = e
            print(' '.join(map(str, arr)))
            return
        else:
            arr[i + 1] = arr[i]
            print(' '.join(map(str, arr)))
    arr[0] = e
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    insertionSort1(n, arr)
