# Migratory Birds
# Determine which type of bird in a flock occurs at the highest frequency.
# 
# https://www.hackerrank.com/challenges/migratory-birds/problem
# 

def migratoryBirds(n, ar):
    # Complete this function
    nb = [0] * 6
    for i in ar:
        nb[i] += 1
    m = max(nb)
    for i, n in enumerate(nb):
        if n == m:
            return i

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
