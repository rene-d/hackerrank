# Determining DNA Health
# Determine which weighted substrings in a subset of substrings can be found in a given string and calculate the string's total weight.
#
# https://www.hackerrank.com/challenges/determining-dna-health/problem
#

class KMP:
    """ Knuth-Morris-Pratt """
    def __init__(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        self.partial = ret = [0]
        self.pattern = pattern

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)

    def search(self, T, overlapping=False):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial, [], 0
        P = self.pattern

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                if overlapping:
                    j = partial[j - 1]
                else:
                    j = 0

        return ret


unhealthiest, healthiest = 10 ** 7, 0

n = input()
genes = [KMP(gene) for gene in input().split()]
health = list(map(int, input().split()))
for _ in range(int(input())):
    first, last, d = input().split()
    first, last, d = [int(first), int(last), str(d)]

    h = 0
    for i in range(first, last + 1):
        p = genes[i].search(d, True)
        h += health[i] * len(p)

    unhealthiest = min(unhealthiest, h)
    healthiest = max(healthiest, h)

print(unhealthiest, healthiest)
