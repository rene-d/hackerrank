"""
Piling Up!

https://www.hackerrank.com/challenges/piling-up/problem
"""

for _ in range(int(input())):
    input()
    lengths = list(map(int, input().split()))
    while len(lengths) >= 2:
        m = max(lengths[0], lengths[-1])
        if lengths[0] == m and lengths[0] >= lengths[1]:
            del lengths[0]
        elif lengths[-1] == m and lengths[-1] >= lengths[-2]:
            del lengths[-1]
        else:
            m = 0
            break
    if len(lengths) == 1 and lengths[0] <= m:
        print("Yes")
    else:
        print("No")
    