"""
Array Manipulation

https://www.hackerrank.com/challenges/crush/problem
"""

if __name__ == "__main__":
    n, m = input().split(' ')
    n, m = int(n), int(m)
 
    data = [0] * (n + 2)
    vmax = 0
    
    """ BRUTE FORCE
    for a0 in range(m):
        a, b, k = input().split(' ')
        a, b, k = int(a), int(b), int(k)
        
        for i in range(a, b + 1):
            v = data[i] + k
            data[i] = v
            if v > vmax:
                vmax = v
    """
    
    # au lieu de faire +k à chaque fois entre [a,b]
    # on mémorise les changements (+k à a et -k après b)
    # et on fait la somme une seule fois
    for a0 in range(m):
        a, b, k = input().split(' ')
        a, b, k = int(a), int(b), int(k)
    
        data[a] += k
        data[b + 1] -= k
    
    v = 0
    for i in range(1, n + 1):
        v += data[i]
        if v > vmax:
            vmax = v
    
    print(vmax)
