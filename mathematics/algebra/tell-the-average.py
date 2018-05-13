# Mathematics > Algebra > Tell the Average
# Tell me average of all list value.
#
# https://www.hackerrank.com/challenges/tell-the-average/problem
# https://www.hackerrank.com/contests/infinitum8/challenges/tell-the-average
#

# l'ordre des élément de L ne change pas le résultat, heureusement
# a+a.b+b = (a+1)(b+1) - 1
# par récurrence, on trouve que S = ∏(Lᵢ+1) - 1

# une autre solution issue de l'égalité précédente:
#   a = 1
#   for b in L: a = (a * (b + 1)) % 1000000007
#   print((a - 1) % 1000000007)
#

_, L = input(), list(map(int, input().split()))

a = 0
for b in L:
    a = a + b + a * b

print(a % 1000000007)
