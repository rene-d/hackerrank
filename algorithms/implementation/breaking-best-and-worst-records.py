# Breaking the Records
# Given an array of Maria's basketball scores all season, determine the number of times she breaks her best and worst records.
# 
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# 

def breakingRecords(score):
    # Complete this function
    nmin, nmax = 0, 0
    smin, smax = score[0], score[0]
    for s in score[1:]:
        if s < smin:
            smin = s
            nmin += 1
        if s > smax:
            smax = s
            nmax += 1        
    return nmax, nmin

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
