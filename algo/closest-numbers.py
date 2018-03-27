# Closest Numbers
# Find the closest numbers in a list.
#
# https://www.hackerrank.com/challenges/closest-numbers/problem
#

def closestNumbers(arr):
    # Complete this function
    arr = sorted(arr)
    m = min(arr[i] - arr[i - 1] for i in range(1, len(arr)))
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == m:
            result.append(arr[i - 1])
            result.append(arr[i])
    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = closestNumbers(arr)
    print(" ".join(map(str, result)))
