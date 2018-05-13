# Sherlock and Divisors
# Help Sherlock in Counting Divisors.
#
# https://www.hackerrank.com/challenges/sherlock-and-divisors/problem
#

# from my eulerlib.py
def diviseurs(n):
    div = [1]
    i = 2
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            div.append(i)
            if i != q:
                div.append(q)
        i += 1
    if n != 1:
        div.append(n)
    return div


def even_divisors(n):
    return sum(1 for d in diviseurs(n) if d % 2 == 0)


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        result = even_divisors(n)
        print(result)
