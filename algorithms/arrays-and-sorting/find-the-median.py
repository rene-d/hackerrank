# Find the Median
# Find the Median in a list of numbers.
#
# https://www.hackerrank.com/challenges/find-the-median/problem
#

def findMedian(arr):
    # la valeur médiane est celle qui partage la liste triée en 2
    return sorted(arr)[len(arr) // 2]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)
