# Counting Sort 2
# Simple version of counting sort.
#
# https://www.hackerrank.com/challenges/countingsort2/problem
#

def countingSort(arr):
    # compte les occurences de x ∈ arr[]
    counts = [0] * 100
    for i in arr:
        counts[i] += 1

    # reconstruit arr[] en utilisant le nombre d'occurences
    j = 0
    for i, n in enumerate(counts):
        while n > 0:
            arr[j] = i
            j += 1
            n -= 1

    return arr


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
