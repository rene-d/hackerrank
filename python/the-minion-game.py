"""
The Minion Game

https://www.hackerrank.com/challenges/the-minion-game/problem
"""


def minion_game(string):
    # your code goes here

    stuart, kevin = 0, 0
    length = len(string)
    
    for i in range(length):
        if string[i] in 'AEIOU':
            kevin += length - i
        else:
            stuart += length - i
    
    if False:
        # non optimisé, trop long si length grand
        substr = []
        for i in range(length):
            for j in range(i, length):
                substr.append(string[i:j + 1])

        scores = dict()
        for i in set(substr):
            pos = 0
            score = 0
            while True:
                pos = string.find(i, pos)
                if pos == -1: break
                pos += 1
                score += 1
            scores[i] = score

        for i, score in scores.items():
            if i[0] in "AEIOU":
                kevin += score
            else:
                stuart += score

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
