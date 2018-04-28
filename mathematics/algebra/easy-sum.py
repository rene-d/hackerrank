# Mathematics > Algebra > Easy sum
# Find the mod sum
#
# https://www.hackerrank.com/challenges/easy-sum/problem
#


def s_brutforce(n, m):
    x = 0
    for i in range(1, n + 1):
        x += i % m
    return x


def s(n, m):
    if m > n:
        # modulo > n: c'est la somme des i de 1 à n
        return n * (n + 1) // 2
    else:
        # sinon:
        # c'est la somme de 0 à m-1 autant de fois qu'il y a m dans n
        # et il faut ajouter la somme de 1 à ce qu'il reste
        q, r = divmod(n, m)
        s = q * (m * (m - 1) // 2)
        s += r * (r + 1) // 2
        return s


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(s(n, m))