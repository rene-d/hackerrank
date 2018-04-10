# Insertion Sort Advanced Analysis
# How many shifts will it take Insertion Sort to sort an array?
#
# https://www.hackerrank.com/challenges/insertion-sort/problem
#

def insertionSort(arr):

      bit = [0] * 10000001
      bit_sum = 0
      count = 0

      for n in arr:
        count += bit_sum
        idx = n
        while idx:
          count -= bit[idx]
          idx -= idx & -idx

        idx = n
        while idx < 10000001:
          bit[idx] += 1
          idx += idx & -idx

        bit_sum += 1

      return count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertionSort(arr)
        print(result)
