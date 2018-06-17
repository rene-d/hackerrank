# Mathematics > Number Theory > Easy math
# Help Johnny in figuring out the value of Y
#
# https://www.hackerrank.com/challenges/easy-math/problem
# https://www.hackerrank.com/contests/101oct13/challenges/easy-math
# challenge id: 1138
#


for _ in range(int(input())):
    n = x = int(input())

    n2 = 0
    while x % 2 == 0:
        n2 += 1
        x //= 2

    # le nombre de 0 est le nombre de 5
    n5 = 0
    while x % 5 == 0:
        n5 += 1
        x //= 5

    if False:
        # nota: on ne doit pas être très loin de l'utilisation
        # de l'indicatrice d'Euler puisque:
        #   a^φ(n) ≡ 1 mod n   avec a,n coprime
        # en prenant a=10 et n=x, ils sont coprime
        # et 10^n-1 = 9999...9 ≡ 0 mod x
        # soit 9/4 * 44444...44 ≡ 0 mod x
        # à un coefficient près (que je ne connais pas), φ(x) = nombre de 4
        a = EulerPhi(x)
    else:
        y = 1
        a = 1
        while y % x != 0:
            y = (y * 10 + 1) % x
            a += 1

    # le nombre de 4 est le nombre de 1, i.e. a
    b = n5
    if n2 - n5 > 2:
        b += n2 - n5 - 2

    print(2 * a + b)
