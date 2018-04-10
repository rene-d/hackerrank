# Hash Tables: Ice Cream Parlor
# Help Sunny and Johnny spend all their money during each trip to the Ice Cream Parlor.
# 
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
# 


def solve(arr, money):
    # Complete this function
    m = {}
    for i, a in enumerate(arr, 1):
        r = money - a
        if r in m:
            print(m[r], i)
            return
        m[a] = i
    

if __name__ == "__main__":
    t = int(input())
    for a0 in range(t):
        money = int(input())
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, money)
