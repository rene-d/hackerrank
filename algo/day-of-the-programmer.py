# Day of the Programmer
# Given year, determine date of the 256th day of the year.
# 
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# 

def solve(year):
    # Complete this function
    if year == 1918:
        return "26.09.1918" # cas spécial de la transition calendrier julien -> grégorien
    if year >= 1918:
        leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    else:
        leap = year % 4 == 0
    if leap:
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)

year = int(input().strip())
result = solve(year)
print(result)
