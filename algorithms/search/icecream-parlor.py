# Ice Cream Parlor
# Help Sunny and Johnny spend all their money during each trip to the Ice Cream Parlor.
#
# https://www.hackerrank.com/challenges/icecream-parlor/problem
#

def icecreamParlor(money, arr):
    # Complete this function
    m = {}
    for i, a in enumerate(arr, 1):
        r = money - a
        if r in m:
            print(m[r], i)
            return
        m[a] = i

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        icecreamParlor(m, arr)
