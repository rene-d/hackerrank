# The Full Counting Sort
# The real counting sort.
#
# https://www.hackerrank.com/challenges/countingsort4/problem
#


if __name__ == "__main__":
    n = int(input())

    # attention à la définition du tableau:
    # [[]] * 100 crée un tableau de 100 fois le même objet [] !
    counts = [[] for i in range(100)]
    for i in range(n):
        x, s = input().split()
        if i < n // 2:
            s = '-'
        counts[int(x)].append(s)

    def y():
        for i in counts:
            for j in i:
                yield j

    print(" ".join(y()))
