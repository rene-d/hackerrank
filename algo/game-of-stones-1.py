# Game of Stones
# A Game of Stones
# 
# https://www.hackerrank.com/challenges/game-of-stones-1/problem
# 

def gameOfStones(n):
    # Complete this function
    return "Second" if n % 7 <= 1 else "First"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        print(result)

"""
It's proof by induction.
The hypothesis: 
For n % 7 in [0, 1], the first player loses, otherwise the first player wins.
The anchor:
Clearly, for 0 or 1 stones, the first player has no move, so he loses. 
For any of 2, 3, 4, 5, or 6 stones, the first player can make a move that leaves 0 or 1 stones for the second player, so the first player wins.
Induction step: 
Now, for a given starting position n we assume that our hypothesis is true for all m < n.
If n % 7 in [0, 1], we can only leave the second player with positions (n - 2) % 7 in [5, 6], (n - 3) % 7 in [4, 5], or (n - 5) % 7 = [2, 3], all of which mean – by induction – that the second player will be in a winning position. Thus, for n % 7 in [0, 1], the first player loses.
If n % 7 in [2, 3, 4, 5, 6], there's always a move to leave the second player with an m % 7 in [0, 1], thus – again by induction – forcing a loss on the second player, leaving the first player to win.
That concludes the proof.
The invariant is, that once a player A can force [0, 1] on player B, A can keep forcing that position, while B cannot force it on A.
"""
