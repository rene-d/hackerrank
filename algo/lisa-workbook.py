# Lisa's Workbook
# A workbook with chapters. Some number of problems per page. How many problems have a number equal to a page's number?
#
# https://www.hackerrank.com/challenges/lisa-workbook/problem
#

# pas compliqué, il faut bien lire et suivre l'énoncé

def workbook(n, k, arr):
    resultat = 0
    page = 0

    # parcourt les chapitres
    for num_pb in arr:
        pb = 1

        # parcourt les pages
        while True:
            page += 1
            if pb <= page < pb + min(num_pb, k):
                resultat += 1

            # il n'y a plus de problème dans ce chapitre
            if num_pb <= k:
                break

            # il y en a encore: décrémente le nombre de problèmes restant
            # et incrémente le numéro du premier problème de la page suivante
            num_pb -= k
            pb += k

    return resultat


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)
