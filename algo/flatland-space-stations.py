# Flatland Space Stations
# Find the maximum distance an astronaut needs to travel to reach the nearest space station.
#
# https://www.hackerrank.com/challenges/flatland-space-stations/problem
#


def flatlandSpaceStations(n, c):

    # trie les space stations
    sp = sorted(c)

    # distence entre la première ville et la première station
    # et distance entre la dernière ville et la dernière station
    r = max(sp[0] - 0, n - 1 - sp[-1])

    for i in range(1, len(sp)):
        # le plus long chemin entre deux stations
        r = max(r, (sp[i] - sp[i - 1]) // 2)
    return r


if __name__ == "__main__":
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    result = flatlandSpaceStations(n, c)
    print(result)
