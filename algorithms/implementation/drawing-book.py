# Drawing Book
#  How many pages does Brie need to turn to get to page p?
#
# https://www.hackerrank.com/challenges/drawing-book/problem
#

# pour résoudre ce challenge du premier coup (i.e. sans tatonner, la formule étant
# forcément une division par 2, on finira bien par tomber sur la bonne), il suffit
# de décrire tous les cas, qui ne sont pas nombreux: le seul ajustement à faire
# concerne la denière page: est-elle numérotée ou non ?

def solve(n, p):
    # depuis la fin:
    if n % 2 == 0:
        # la dernière page est blanche
        # nombre de pages à tourner:
        # p=n => 0
        # p=n-1 ou n-2 => 1
        # p=n-3 ou n-4 => 2     => (n-p+1)//2 en partant de la fin
        fin = (n - p + 1) // 2
    else:
        # la dernière page est numérotée
        # p=n ou n-1 => 0
        # p=n-2 ou n-3 => 1
        # p=n-3 ou n-4 => 2     => (n-p+1)//2 en partant de la fin
        fin = (n - p) // 2

    # depuis le début:
    # p=1 => 0
    # p=2 ou 3 => 1
    # p=4 ou 5 => 2             => p//2 en partant du début
    debut = p // 2

    return min(debut, fin)


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
