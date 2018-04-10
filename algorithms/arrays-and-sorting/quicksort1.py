# Quicksort 1 - Partition
# Perform the first step of Quicksort: partitioning an array.
#
# https://www.hackerrank.com/challenges/quicksort1/problem
#

def quickSort(arr):
    # partitionne arr[] autour de pivot
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
    return left + [pivot] + right

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))
