# Algorithms > Greedy > Minimum Absolute Difference in an Array
# Given a list of integers, calculate their differences and find the difference with the smallest absolute value.
#
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
#


def minimumAbsoluteDifference(n, arr):
    # différence minimale entre deux entiers consécutifs de la liste ordonnée
    arr = sorted(arr)
    return min(abs(arr[i] - arr[i + 1]) for i in range(n - 1))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
