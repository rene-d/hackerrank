# Algorithms > Bit Manipulation > A or B
# A or B = C
#
# https://www.hackerrank.com/challenges/aorb/problem
#


def aOrB16(a, b, c):
    n = 0
    i = 0
    na, nb = 0, 0

    for i in range(16):
        a, ra = divmod(a, 2)
        b, rb = divmod(b, 2)
        c, rc = divmod(c, 2)
        if rc == 0:
            # il faut changer les 1 en 0 dans a et/ou b
            n += ra + rb

        else:
            # si 0 dans a et b, il faut mettre 1 dans l'un ou l'autre
            n += 1 - (ra | rb)

            if (ra | rb) == 0: rb = 1
            na |= ra << i
            nb |= rb << i

    return na, nb, n


def precompute():
    d = [0] * 4096
    for a in range(16):
        for b in range(16):
            for c in range(16):
                d[a * 256 + b * 16 + c] = aOrB16(a, b, c)
    return d


# https://oeis.org/A000120
# nombre de 1 dans l'écriture binaire de n ou "Hamming weight"
nb_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

aOrB_table = precompute()


def aOrB(k, a, b, c):

    la = len(a)
    lb = len(b)
    lc = len(c)

    maxlen = max(la, lb, lc)
    a = [0] * (maxlen - la) + list(int(i, 16) for i in a)
    b = [0] * (maxlen - lb) + list(int(i, 16) for i in b)
    c = [0] * (maxlen - lc) + list(int(i, 16) for i in c)

    n = k
    for i in range(maxlen):
        ra, rb, rn = aOrB_table[a[i] * 256 + b[i] * 16 + c[i]]
        n -= rn
        if n < 0:
            print(-1)
            return
        a[i] = ra
        b[i] = rb

    if n > 0:
        # on peut encore annuler n bits entre A' et B'
        # (ceux qui valent 1 dans les 2 nombres, en commençant par A')

        for i in range(maxlen):
            if a[i] == 0: continue
            for j in range(3, -1, -1):

                if n >= 2 and a[i] & (1 << j) != 0 and b[i] & (1 << j) == 0:
                    # on peut faire passer 1 bit de A' vers B'
                    a[i] &= 15 - (1 << j)
                    b[i] |= (1 << j)
                    n -= 2

                elif a[i] & b[i] & (1 << j) != 0:
                    # on peut annuler 1 bit de A'
                    a[i] &= 15 - (1 << j)
                    n -= 1

                if n == 0: break
            if n == 0: break

    def to_hex(a):
        i = 0
        while i < maxlen - 1 and a[i] == 0:
            i += 1
        while i < maxlen:
            yield "0123456789ABCDEF"[a[i]]
            i += 1

    print(''.join(to_hex(a)))
    print(''.join(to_hex(b)))


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        k = int(input())

        a = input().strip()
        b = input().strip()
        c = input().strip()

        aOrB(k, a, b, c)
