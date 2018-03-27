# Sequence Equation
# Find some y satisfying p(p(y)) = x for each x from 1 to n.
#
# https://www.hackerrank.com/challenges/permutation-equation/problem
#

def permutationEquation(p):
    # Complete this function
    n = len(p)
    q = [0] * n

    # p(p(𝓎)) = 𝓍 (au décalage de 1 près)
    for i in range(0, n):
        q[p[p[i] - 1] - 1] = i + 1
    return q


if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))
