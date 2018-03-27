# Strange Counter
# Print the value displayed by the counter at a given time, $t$.
#
# https://www.hackerrank.com/challenges/strange-code/problem
#

import math

def strangeCode(t):
    # Complete this function

    # 3 + 6 + 12 + 24 + 48 + ...
    # 3 * (1 + 2 + 4 + 8 + ...)
    # 3 * (2^n - 1) <= t < 3 * (2^(n+1) - 1)
    # 2^n <= t / 3 + 1
    # n <= log(t / 3 + 1) / log(2) < n + 1

    t -= 1
    n = math.floor(math.log2(t / 3 + 1))

    # bornes de la colonne : ]a, b]
    # a = 3 * (2 ** n - 1)
    b = 3 * (2 ** (n + 1) - 1)

    return b - t


if __name__ == "__main__":
    t = int(input().strip())
    result = strangeCode(t)
    print(result)
