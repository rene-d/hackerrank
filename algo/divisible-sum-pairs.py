# Divisible Sum Pairs
# Count the number of pairs in an array having sums that are evenly divisible by a given number. 
# 
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# 

def divisibleSumPairs(n, k, ar):
    # Complete this function
    nb = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                nb += 1
    return nb

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
