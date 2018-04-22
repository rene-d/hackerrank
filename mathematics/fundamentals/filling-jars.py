# Mathematics > Fundamentals > Filling Jars
# Perform the multiple queries on the list. And print average. - 20 Points
#
# https://www.hackerrank.com/challenges/filling-jars/problem
#

# dans ce challenge, nul besoin de calculer les contenus de chaque jarre
# il suffit de calculer une somme globale
# sinon c'est trop lent

n, m = map(int, input().split())
sum_k = 0
for _ in range(m):
    a, b, k = map(int, input().split())
    sum_k += k * (b - a + 1)
print(sum_k // n)
