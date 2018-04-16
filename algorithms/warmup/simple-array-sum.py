# Algorithms > Warmup > Simple Array Sum
# Calculate the sum of integers in an array. 
# 
# https://www.hackerrank.com/challenges/simple-array-sum/problem
# 



#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
