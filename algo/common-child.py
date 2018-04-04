# Common Child
# Given two strings a and b of equal length, what's the longest string (s) that can be constructed such that s is a child to both a and b?
#
# https://www.hackerrank.com/challenges/common-child/problem
#

# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

# à exécuter avec PyPy3, sinon trop lent

def lcs_length(s1, s2):
    m = len(s1)
    n = len(s2)
    C = [0] * (m + 1) * (n + 1)
    K = n + 1

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                C[i + 1 + (j + 1) * K] = C[i + j * K] + 1
            else:
                C[i + 1 + (j + 1) * K] = max(C[(i + 1) + j * K], C[i + (j + 1) * K])
    return C[m + n * K]


s1 = input().strip()
s2 = input().strip()
result = lcs_length(s1, s2)
print(result)
