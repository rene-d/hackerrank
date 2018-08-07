# Mathematics > Number Theory > Strange numbers
# How many strange numbers belong to interval [L, R]?
#
# https://www.hackerrank.com/challenges/strange-numbers/problem
# https://www.hackerrank.com/contests/w11/challenges/strange-numbers
# challenge id: 3082
#

# la grosse astuce consiste à prendre le problème à l'envers:
# -> c'est facile de tester si un nombre est «strange»
# -> on en déduit comment ils sont construits

# problème amusant mais pas très mathématique


def forensic():
    """ brute force / comprendre le problème ... """

    def is_strange(i):

        l = len(str(i))
        if l == 1:
            return True
        if i % l != 0:
            return False

        return is_strange(i // l)

    def construction(i):
        s = str(i)
        l = len(s)
        if l == 1: return "1" + " (" + s + ")"
        return str(l) + " " + construction(i // l)

    n = 0
    l = 0
    for i in range(100, 100000):
        if is_strange(i):
            if l != len(str(i)):
                l = len(str(i))
                n = 0
            n += 1
            print("{:3} {:10} {}".format(n, i, construction(i)))


# résolution du challenge

stranges = []


def make_strange(n):
    """ construction de tous les nombres «strange» de longueur ≤ 18 à partir de n """
    stranges.append(n)

    l = len(str(n))
    if l > 18:
        return

    for i in range(l + 1, l + 5):
        m = n
        while len(str(m * i)) == i:
            m *= i
            make_strange(m)


for n in range(0, 10):
    make_strange(n)

stranges.sort()


# c'est parti !
if __name__ == '__main__':
    for _ in range(int(input())):
        L, R = map(int, input().split())
        print(sum(1 for i in stranges if L <= i <= R))
