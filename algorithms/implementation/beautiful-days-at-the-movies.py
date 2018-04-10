# Beautiful Days at the Movies
# Find the number of beautiful days.
# 
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# 

def beautifulDays(i, j, k):
    # Complete this function
    return sum(1 for n in range(i, j + 1) 
               if abs(n - int(''.join(reversed(str(n))))) % k == 0)


if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
