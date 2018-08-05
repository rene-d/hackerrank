# Ad Infinitum 11 - Math Programming Contest > Fibonacci GCD Again
# Compute GCDs involving Fibonacci numbers... again.
#
# https://www.hackerrank.com/contests/infinitum11/challenges/fibonacci-gcd-again
# challenge id: 5105
#

from math import gcd


def multm(A, B, MOD):
    """ produit matriciel: A * B """
    a00, a10, a01, a11 = A
    b00, b10, b01, b11 = B
    return [(a00 * b00 + a10 * b01) % MOD, (a00 * b10 + a10 * b11) % MOD,
            (a01 * b00 + a11 * b01) % MOD, (a01 * b10 + a11 * b11) % MOD]


def multv(A, V, MOD):
    """ produit matrice/vecteur: A * V """
    a00, a10, a01, a11 = A
    b0, b1 = V
    return [(a00 * b0 + a10 * b1) % MOD,
            (a01 * b0 + a11 * b1) % MOD]


def power(M, k, MOD):
    """ fast exponentiation M^k """
    P = [1, 0,
         0, 1]

    if k == 0:
        return P
    if k == 1:
        return M

    while k != 0:
        if k % 2 == 1:
            P = multm(P, M, MOD)
        M = multm(M, M, MOD)
        k //= 2
    return P


def F(n, MOD):
    A = [1, 1, 1, 0]
    An = power(A, n, MOD)
    F0 = [1, 0]
    Fn = multv(An, F0, MOD)
    return Fn[1], Fn[0]


def solve():
    for _ in range(int(input())):
        N, a0, a1, a2, b0, b1, b2, M = map(int, input().split())

        # calcul de G = gcd(a0*Fn0+a1*Fn1+a2*Fn2, b0*Fn0+b1*Fn1+b2*Fn2)

        # a0*Fn0+a1*Fn1+a2*Fn2 = a0*Fn0+a1*Fn1+a2*(Fn0+Fn1) = (a0+a2)*Fn0+(a1+a2)*Fn1
        a0 += a2
        a1 += a2
        b0 += b2
        b1 += b2
        # d'où G = gcd(a0*Fn0+a1*Fn1, b0*Fn0+b1*Fn1)   (a0,a1,b0,b1 modifiés)

        # trouvons (a0', a1') et b0' tels que G = gcd(a0'*Fn0+b0'*Fn1, b0'*Fn0)
        # par l'algorithme d'Euclide: gcd(a, b)=gcd(b, a mod b)
        # on applique l'algo jusqu'à b1'=0

        print(a0, a1, b0, b1)

        if a1 == 0:
            a0, a1, b0, b1 = b0, b1, a0, a1

        while b1 != 0:
            if b1 < a1:
                a0, a1, b0, b1 = b0, b1, a0, a1

            q = b1 // a1
            b0, b1 = b0 - a0 * q, b1 - a1 * q

        print(a0, a1, b0, b1)

        # ici G = gcd(a0*Fn0+a1*Fn1, b0*Fn0)

        if b0 == 0:
            # simplification!
            # G = gcd(a0*Fn0+a1*Fn1, 0)
            # gcd(a, 0) = a
            Fn0, Fn1 = F(N, M)
            r = (a0 * Fn0 + a1 * Fn1) % M

        elif a1 == 0:
            # simplification!
            # G = gcd(a0*Fn0, b0*Fn0)
            # = gcd(a0, b0) * Fn0
            Fn0, _ = F(N, M)
            r = (gcd(a0, b0) * Fn0) % M

        else:
            # cas général...
            g = gcd(a1, F(N, a1)[0])
            print(g)

            Fn0, Fn1 = F(N, b0 * g)

            r = gcd(a0 * Fn0 + a1 * Fn1, b0 * g) % M

        print(r)

        #Fn0 = 77310304634413492993758144743538184801550997720924982727487206270083963211589736272393893
        #Fn1 = 125090700579089545268174422433569433531336921195894847055310250098200676237081739043824861
        #debug(N, Fn0, Fn1, sep='\n')
        #print(gcd(a0 * Fn0 + a1 * Fn1, b0 * Fn0 + b1 * Fn1) % M)

solve()