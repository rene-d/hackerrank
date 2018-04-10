# Non-Divisible Subset
# Find the size of the maximal non-divisible subset.
#
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
#


def nonDivisibleSubset(k, arr):
    # algorithme:
    # - pour que Ai + Aj soit divisibe par k, il faut que :
    #      Ai % k + Aj % k = k
    # - on compte les nombres Ai qui ont le même reste de la division par k
    #   restes[r] = nombre de Ai tel que Ai % k == r
    # - pour un reste donné r, il faudra éliminer les nombres du groupe r
    #   ou les nombres du groupe k-r : on gardera les plus nombreux
    # - cas particulier de r == 0:
    #   ce sont les diviseurs de k. S'il y en a qu'un on peut le garder
    #   puisqu'aucun autre nombre ne pourra s'ajouter pour donner une somme
    #   divisible par k. S'il y en plus qu'un, on ne peut garder aucun.
    # - si k est pair, même chose: un seul diviseur de k/2 => on le garde,
    #   plus qu'un diviseur de k/2 => on les rejette tous

    restes = [0] * k
    for i in arr:
        restes[i % k] += 1

    nb = min(restes[0], 1)
    for r in range(1, k // 2 + 1):
        if r != k - r:
            nb += max(restes[r], restes[k - r])
        else:
            nb += min(1, restes[r])

    return nb


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
