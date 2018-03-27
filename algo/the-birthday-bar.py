# Birthday Chocolate
# Given an array of integers, find the number of subarrays of length k having sum s.
# 
# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# 

def solve(n, s, d, m):
    # Complete this function
    return sum(1 for i in range(len(s) - m + 1) if sum(s[i:i + m]) == d)


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
