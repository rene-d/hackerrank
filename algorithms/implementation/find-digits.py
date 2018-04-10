# Find Digits
# Calculate the number of digits in an integer that evenly divide it.
#
# https://www.hackerrank.com/challenges/find-digits/problem
#


def findDigits(n):
    # Complete this function
    return sum(1 for d in str(n) if d != "0" and n % int(d) == 0)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
