# Intro to Tutorial Challenges
# Introduction to the Tutorial Challenges
#
# https://www.hackerrank.com/challenges/tutorial-intro/problem
#

#
# dichotomie
#
def introTutorial(x, a):

    first = 0
    last = len(a) - 1

    while first <= last:
        i = (first + last) // 2
        if a[i] == x:
            return i
        elif a[i] > x:
            last = i - 1
        else:
            first = i + 1

    return first


if __name__ == "__main__":
    V = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    result = introTutorial(V, arr)
    print(result)
