# Mathematics > Number Theory > Manasa and Factorials
# Think about number of zeros in k!
#
# https://www.hackerrank.com/challenges/manasa-and-factorials/problem
# https://www.hackerrank.com/contests/infinitum-apr14/challenges/manasa-and-factorials
#


def count5(n):
    sum = 0
    product = 1
    while product < n:
        product *= 5
        sum += n // product
    return sum


for _ in range(int(input())):
    n = int(input())

    # chaque mutiple de 5 ajoute un 0 (en fait de 2 et 5 mais il y a plus de mutiples de 2 que de 5 dans n!)
    # et plus généralement:
    # chaque mutiple de 5^k ajoute k 0

    # la réponse est entre 4n et 5n
    # et multiple de 5
    j = (4 * n + 4) // 5 * 5

    while count5(j) < n:
        j += 5

    print(j)
