# Kangaroo
# Can two kangaroo meet after making the same number of jumps?
# 
# https://www.hackerrank.com/challenges/kangaroo/problem
#

def kangaroo(x1, v1, x2, v2):
    # x1+k*v1 = x2+k*v2 => x1-x2=k*(v2-v1), k>0
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    q, r = divmod(x1 - x2, v2 - v1)
    if r == 0 and q > 0:
        return 'YES'
    else:
        return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
