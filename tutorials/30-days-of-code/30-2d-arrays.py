# Tutorials > 30 Days of Code > Day 11: 2D Arrays
# Find the maximum sum of any hourglass in a 2D-Array.
#
# https://www.hackerrank.com/challenges/30-2d-arrays/problem
#


def array2D(arr):
    resulat = -100
    for i in range(0, 4):
        for j in range(0, 4):
            s = sum(arr[i][j:j + 3])
            s += arr[i + 1][j + 1]
            s += sum(arr[i + 2][j:j + 3])
            if s > resulat:
                resulat = s
    return resulat


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().split())))
    result = array2D(arr)
    print(result)
