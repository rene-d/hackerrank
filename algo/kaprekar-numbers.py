# Modified Kaprekar Numbers
# Print kaprekar numbers in the given range
#
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
#


def kaprekarNumbers(p, q):
    # Complete this function
    found = False
    for i in range(p, q + 1):
        s = str(i * i)
        d = len(s) // 2
        l = int(s[:d]) if d > 0 else 0
        r = int(s[d:])
        if l + r == i:
            yield i
            found = True
    if not found:
        yield "INVALID RANGE"


if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    print (" ".join(map(str, kaprekarNumbers(p, q))))
