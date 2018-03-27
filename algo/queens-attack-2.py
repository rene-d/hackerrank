# Queen's Attack II
# Find the number of squares the queen can attack.
# 
# https://www.hackerrank.com/challenges/queens-attack-2/problem
# 


def queensAttack(n, k, r_q, c_q, obstacles):
    # Complete this function

    a_d = n - c_q 
    a_g = c_q - 1
    a_h = r_q - 1
    a_b = n - r_q
    a_bd = min(n - r_q, n - c_q)
    a_bg = min(n - r_q, c_q - 1)
    a_hd = min(r_q - 1, n - c_q)
    a_hg = min(r_q - 1, c_q - 1)

    for o in obstacles:
        r, c = o

        if r == r_q:
            if c > c_q:     # droite
                a_d = min(a_d, c - c_q - 1)
            else:           # gauche
                a_g = min(a_g, c_q - c - 1)

        elif c == c_q:
            if r > r_q:     # bas
                a_b = min(a_b, r - r_q - 1)
            else:           # haut
                a_h = min(a_h, r_q - r - 1)

        elif c - c_q == r - r_q:
            if c > c_q:    # bas droite
                a_bd = min(a_bd, min(r - r_q - 1, c - c_q - 1))
            else:           # haut gauche
                a_hg = min(a_hg, min(r_q - r - 1, c_q - c - 1))

        elif c - c_q == r_q - r:
            if c > c_q:     # haut droite
                a_hd = min(a_hd, min(r_q - r - 1, c - c_q - 1))
            else:           # bas gauche
                a_bg = min(a_bg, min(r - r_q - 1, c_q - c - 1))
                
    return a_d + a_g + a_h + a_b + a_bd + a_bg + a_hd + a_hg


def queensAttack0(n, k, r_q, c_q, obstacles):
    # Complete this function
    
    c_q -= 1
    r_q -= 1
    
    chess = [True] * (n * n)
    a = 0
    
    def xy(c, r):
        ok = c < n and r < n and c >= 0 and r >= 0 and chess[c + r * n]
        return ok
    
    def check(ic, ir):
        nonlocal a
        i = 1
        while xy(c_q + ic * i, r_q + ir * i):
            i += 1
            a += 1    
    
    for o in obstacles:
        chess[o[1] - 1 + n * (o[0] - 1)] = False
    
    check(0, 1)         # vers le bas
    check(0, -1)        # vers le haut
    check(1, 0)         # vers la droite
    check(-1, 0)        # vers la gauche
    check(1, 1)         # bas/droite
    check(-1, 1)        # bas/gauche
    check(1, -1)        # haut/droite
    check(-1, -1)       # haut/gauche

    return a


if __name__ == "__main__":
    n, k = map(int, input().split())
    r_q, c_q = map(int, input().split())
    obstacles = []
    for _ in range(k):
       obstacles.append(list(map(int, input().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
