# Sherlock and Squares
# Find the count of square numbers between A and B
#
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
#


def squares(a, b):
    # Complete this function

    # Il y a deux manières de faire:
    # - soit on cherche tous les carrés entre a eb b
    # - soit on vérifie que les nombres entre a et b sont des carrés
    # La deuxième solution est trop lente, surtout avec les conditions de l'énoncé
    # 1 ≤ a ≤ b ≤ 10⁹
    nb = 0

    r = int(a ** 0.5)
    if a <= r * r <= b:
        nb += 1
    while True:
        r += 1
        if r * r <= b:
            nb += 1
        else:
            break
    return nb

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)
