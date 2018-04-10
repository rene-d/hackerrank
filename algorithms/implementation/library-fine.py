# Library Fine
# Help your library calculate fees for late books!
#
# https://www.hackerrank.com/challenges/library-fine/problem
#


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Complete this function
    if y1 > y2:
        return 10000                    #  plus d'un an de retard
    elif y1 == y2:
        if m1 > m2:
            return (m1 - m2) * 500      # plus d'un mois de retard
        elif m1 == m2:
            if d1 > d2:
                return (d1 - d2) * 15   # retard dans le même mois
    return 0    # retour avant ou à l'échéance


if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
