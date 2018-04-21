# Algorithms > Bit Manipulation > Counter game
# Louise and Richard play a game, find the winner of the game.
#
# https://www.hackerrank.com/challenges/counter-game/problem
#

pow2 = [1 << i for i in range(63, -1, -1)]

def counterGame(n):
    player = 0

    while n != 1:
        # print( ["Louise", "Richard"][player],n)
        for i in pow2:
            if n == i:
                n = n // 2
                if n != 1:
                    player = 1 - player
                break
            elif n & i == i:
                n = n - i
                if n != 1:
                    player = 1 - player
                break
    return ["Louise", "Richard"][player]

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = counterGame(n)
        print(result)
