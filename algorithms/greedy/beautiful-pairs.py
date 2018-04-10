# Beautiful Pairs
# Change an element of B and calculate the number of pairwise disjoint beautiful pairs.
#
# https://www.hackerrank.com/challenges/beautiful-pairs/problem
#

def beautifulPairs(A, B):
    # compte les nombres de A
    n = [0] * 1001
    for i in A:
        n[i] += 1

    # compare avec les nombres de B et compte
    pairs = 0
    for i in B:
        if n[i] > 0:
            n[i] -= 1
            pairs += 1

    # si tous les nombres sont en paire (A==B)
    # il faut sacrifier un nombre (cf. énoncé)
    # sinon, on peut gagner une paire
    if pairs == len(B):
        pairs -= 1
    else:
        pairs += 1

    return pairs


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = beautifulPairs(A, B)
    print(result)
