"""
Mini-Max Sum

https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

def miniMaxSum(arr):
    # Complete this function
    arr = sorted(arr)
    print(sum(arr[0:4]), sum(arr[1:5]))
    
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
