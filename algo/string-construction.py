# String Construction
# Find the minimum cost of copying string s.
#
# https://www.hackerrank.com/challenges/string-construction/problem
#

# aucun intérêt: la réponse est: le nombre de caractères différents!

def stringConstruction(s):
    return len(set(s))

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
