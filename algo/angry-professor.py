# Angry Professor
# Decide whether or not the class will be canceled based on the arrival times of its students.
# 
# https://www.hackerrank.com/challenges/angry-professor/problem
# 

import sys

def angryProfessor(k, a):
    # Complete this function
    # il faut compter le nombre de temps négatifs ou nuls
    if sum(1 for i in a if i <= 0) >= k: 
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)

