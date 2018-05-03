# Python > Sets > Introduction to Sets
# Use the set tool to compute the average.
#
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#

def average(array):
    # your code goes here
    a = set(array)
    return sum(a) / len(a)

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
