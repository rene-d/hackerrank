# Picking Numbers
# What's the largest size subset can you choose from an array such that the difference between any two integers is not bigger than 1?
#
# https://www.hackerrank.com/challenges/picking-numbers/problem
#

def pickingNumbers(a):
    # Complete this function

    # pour chaque nombre i de a, je cherche combien de nombres
    # sont égaux ou +1
    return max(sum(1 for j in a if 0 <= j - i <= 1) for i in a)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = pickingNumbers(a)
    print(result)
