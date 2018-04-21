# Data Structures > Stacks > Largest Rectangle
# Given n buildings, find the largest rectangular area possible by joining consecutive K buildings.
#
# https://www.hackerrank.com/challenges/largest-rectangle/problem
#


def largestRectangle(heights):
    # pile des index des plus hautes tours
    stack = [-1]
    max = 0

    i = 0
    while i < n:
        h = heights[i]
        # ajoute la hauteur si elle est supérieure à la plus haute hauteur de la stack
        if len(stack) == 1 or h >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            # sinon, calcule la surface entre la plus basse tour
            # qui est à l'index top()-1 (peut être le pseudo index -1)
            # et la dernière qui est à l'index i
            m = heights[stack.pop()] * (i - stack[-1] - 1)
            if m > max:
                max = m

    # vide la stack avec le même algo
    while len(stack) > 1:
        m = heights[stack.pop()] * (i - stack[-1] - 1)
        if m > max:
            max = m

    return max


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))
    result = largestRectangle(h)
    print(result)
