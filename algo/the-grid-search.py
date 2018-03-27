# The Grid Search
# Given a 2D array of digits, try to find a given 2D grid pattern of digits within it.
#
# https://www.hackerrank.com/challenges/the-grid-search/problem
#


def gridSearch(G, P):

    # on cherche dans toute les lignes de G
    i = 0
    while i <= len(G) - len(P):
        p0 = 0

        while True:
            j = 0
            i0 = i
            # cherche si P[0] se trouve dans la ligne courante de G
            p = G[i0].find(P[j], p0)
            if p == -1:
                break

            # cherche le reste de P, à la même position
            # (OK pas optimisé, mais plus clair à écrire!)
            while j < len(P) and i0 < len(G) and p == G[i0].find(P[j], p0):
                i0 += 1
                j += 1

            if j == len(P):
                return "YES"

            # le motif P[0] peut se retrouver plus loin dans la ligne...
            p0 = p + 1

        i += 1

    return "NO"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P)
        print(result)
