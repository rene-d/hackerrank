# Counting Sort 1
# Count the number of times each value appears.
#
# https://www.hackerrank.com/challenges/countingsort1/problem
#


def countingSort(arr):
    # compte les occurences de arr[i] ∈ [0, 99]
    counts = [0] * 100
    for i in arr:
        counts[i] += 1
    return counts

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
