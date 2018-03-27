# Running Time of Algorithms
# The running time of Algorithms in general and Insertion Sort in particular.
#
# https://www.hackerrank.com/challenges/runningtime/problem
#

def runningTime(n, arr):
    nb = 0
    for i in range(1, n):
        j = i
        k = arr[i]
        while j > 0 and k < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
            nb += 1
        arr[j] = k
    return nb


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(n, arr)
    print(result)
