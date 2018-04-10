# Grading Students
# Round student grades according to Sam's rules.
# 
# https://www.hackerrank.com/challenges/grading/problem
# 

import sys

def solve(grades):
    # Complete this function
    r = []
    for g in grades:
        if g >= 38:
            if ((g + 4) // 5) * 5 - g < 3: g = ((g + 4) // 5) * 5
        r.append(g)
    return r

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



