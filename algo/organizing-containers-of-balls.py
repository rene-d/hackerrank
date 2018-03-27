# Organizing Containers of Balls
# Determine if David can perform some sequence of swap operations such that each container holds one distinct type of ball.
#
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
#

def organizingContainers(containers):
    # somme des lignes == somme des colonnes ?
    return sorted(map(sum, containers)) == sorted(map(sum, zip(*containers)))

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        containers = []
        for _ in range(n):
            containers.append(list(map(int, input().split())))
        result = organizingContainers(containers)
        print("Possible" if result else "Impossible")
