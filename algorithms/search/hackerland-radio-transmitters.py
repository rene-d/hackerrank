# Algorithms > Search > Hackerland Radio Transmitters
# Find the minimum number of radio transmitters needed to cover all the houses in Hackerland!
#
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
#


def hackerlandRadioTransmitters(n, x, k):
    x = sorted(x)
    nb = 0
    i = 0
    while i < n:

        # essaie de placer l'émetteur le plus loin possible vers la droite
        portee = x[i] + k       # on cherche vers la droite le point qui couvre i
        while i < n and x[i] <= portee: i += 1
        i -= 1

        # on place l'émetteur sur le point i
        nb += 1

        # saute les points couverts à droite
        portee = x[i] + k       # on saute tous les points couverts par l'émetteur en ri
        while i < n and x[i] <= portee: i += 1

    return nb


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(n, x, k)
    print(result)
