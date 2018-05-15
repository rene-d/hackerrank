# Mathematics > Probability > Random number generator
# what's the probability that x + y is less than C?
#
# https://www.hackerrank.com/challenges/random-number-generator/problem
#

# la probabilité est le rapport de la surface de l'intersection entre
# le triangle isocèle rectangle (0,c,c) et le rectangle (0,0,a,b)
# avec l'aire du rectangle

from fractions import Fraction

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a + b <= c:
        # le rectangle est entièrement inclus dans le triangle
        print("1/1")
    else:
        if a > b:
            a, b = b, a

        if c < a:
            # le triangle est entièrement inclus dans le rectangle
            #  ___________
            #  |          |
            # a|\         |
            #  |_\________|
            #   c    b
            p = Fraction(c * c, 2 * a * b)
        elif a <= c < b:
            # intersetion: trapèze
            p = Fraction((2 * c - a) * a, 2 * a * b)
            #  _______
            #  |      \
            # a|       \
            #  |________\
            #      c
        else:
            # intersection: complément du triangle isocèle de côté a+b-c
            #  _________
            #  |        \
            # a|         |
            #  |_________|
            #       b
            p = 1 - Fraction((a + b - c) ** 2, 2 * a * b)

        print(p)
