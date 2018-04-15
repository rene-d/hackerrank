# Mathematics > Algebra > Difference and Product
# Answer a question about Difference and Product
# 
# https://www.hackerrank.com/challenges/difference-and-product/problem
# 


from math import sqrt

for _ in range(int(input())):
    d, p = map(int, input().split())
    
    # une valeur absolue ne peut pas être négative
    if d < 0:
        print(0)
        continue
        
    nb = 0
    
    # d = a - b
    # p = a * b
    
    # a = d + b
    # p = (d + b) * b
    # b * b + d * b - p = 0
    # b = (-d +- sqrt(d * d + 4 * p)) / 2
    D = d * d + 4 * p

    # discriminant négatif: aucune solution
    if D < 0:
        print(0)
        continue
    
    b = int((-d - sqrt(D)) / 2)
    a = d + b
    if a * b == p:         
        nb += 1
        # a et b différents: 2 solutions (en intervertissant a et b)
        if a != b:
            nb += 1
    
    # discriminant nul: une seule solution
    if D != 0:
        b = int((-d + sqrt(D)) / 2)
        a = d + b
        if a * b == p: 
            nb += 1
            if a != b:
                nb += 1
                    
    print(nb)
    