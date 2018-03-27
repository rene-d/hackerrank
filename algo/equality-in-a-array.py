# Equalize the Array
# Delete a minimal number of elements from an array so that all elements of the modified array are equal to one another.
#
# https://www.hackerrank.com/challenges/equality-in-a-array/problem
#

# il faut déterminer quel est l'élément le plus fréquent dans le tableau:
# ça minimisera le nombre d'éléments à retirer pour garder la même valeur

def equalizeArray(arr):
    nb = {}  # defaultdict(int)
    nmax = 0
    for i in arr:
        n = nb.get(i, 0) + 1
        if n > nmax:
            nmax = n
        nb[i] = n
    return len(arr) - nmax


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
