"""
Nested Lists

https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    scores = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score in scores:
            scores[score].append(name)
        else:
            scores[score] = [name]

    for name in sorted(scores[sorted(scores.keys())[1]]):
        print(name)
