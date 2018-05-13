# Best Divisor
# Find the best divisor of the number!
#
# https://www.hackerrank.com/challenges/best-divisor/problem
#


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


n = int(input())
r = -max((sum(int(i) for i in str(d)), -d) for d in diviseurs(n))[1]
print(r)
