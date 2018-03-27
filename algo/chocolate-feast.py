# Chocolate Feast
# Calculate the number of chocolates that can be bought following the given conditions.
#
# https://www.hackerrank.com/challenges/chocolate-feast/problem
#

def chocolateFeast(n, c, m):
    # Complete this function
    wrappers = choco = n // c   # nombre de choco achetés
    while wrappers >= m:        # il a assez d'emballage pour échanger un choco
        wrappers -= m           # échange m wrappers contre
        choco += 1              # un choco
        wrappers += 1           # et il récupère un emballage
    return choco

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)
