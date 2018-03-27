# Beautiful Triplets
#
#
# https://www.hackerrank.com/challenges/beautiful-triplets/problem
#

def beautifulTriplets(d, arr):

    # utilise une indirection pour vérifier l'existence du triplet
    # (sinon ça risque d'être trop lent). ici algo en O(n)

    numbers = [False] * (20000 + 1)
    nb = 0

    for a in arr:
        # a-t-on un triplet ?
        if a - 2 * d >= 0 and numbers[a - d] and numbers[a - 2 * d]:
            nb += 1
        # mémorise la présence du nombre
        numbers[a] = True
    return nb


if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    result = beautifulTriplets(d, arr)
    print(result)
