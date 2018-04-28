# Mathematics > Number Theory > Constructing a Number
# Construct a number divisible by 3 from the given numbers by reordering their digits.
#
# https://www.hackerrank.com/challenges/constructing-a-number/problem
#

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.
    s = sum(sum(int(d) for d in str(i)) for i in a)
    return "Yes" if s % 3 == 0 else "No"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        result = canConstruct(a)
        print(result)
