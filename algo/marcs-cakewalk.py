# Marc's Cakewalk
# Find the minimum number of miles Marc must walk to burn the calories consumed from eating cupcakes.
#
# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
#

def marcsCakewalk(calorie):
    # Complete this function
    c = 0
    p = 1
    for i in sorted(calorie, reverse=True):
        c += p * i
        p *= 2
    return c

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)