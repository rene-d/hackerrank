# Almost Sorted
# Sort an array by either swapping or reversing a segment
# 
# https://www.hackerrank.com/challenges/almost-sorted/problem
# 
#!/bin/python3

import sys


def debug(*kw):
    #sys.stderr.write(' '.join(map(repr, kw)) + '\n')
    pass

def almostSorted(arr):
    # Complete this function
    
    l = len(arr)

    # évite des tas de test de débordement
    arr.insert(0, -1)
    arr.append(1000001)
    
    debug(arr, l)
    
    def increasing(i):
        while i <= l and arr[i] < arr[i + 1]:
            i += 1
        return i

    def decreasing(i):
        while i <= l and arr[i] > arr[i + 1]:
            i += 1
        return i
    
    # cherche la première suite croissante
    i = increasing(1)
    if i == l: 
        print("yes")
        return
    
    # ici les éléments [1..i] sont croissants  
    debug("croissants", arr[1:i+1])
    
    j = decreasing(i)        
    
    # ici [i..j] sont décroissants        
    debug("décroissants", arr[i:j+1])

    if j == i + 1:
        # un seul élément décroît:
        # cherche un deuxième, nécessaire pour swap arr[i]
        
        m = increasing(j)
        debug("croissants", arr[j:m+1])
        
        n = decreasing(m)
        debug("décroissants", arr[m:n+1])

        
        if m == l+1 and n == l+1:
            if arr[i-1] < arr[j] < arr[i] < arr[j + 1]:
                arr[j], arr[i] = arr[i], arr[j]
                debug(arr)

                print("yes")
                print("swap", i, j)
                return    
        
        if n == m + 1:
            # un seul candidat: arr[n]
            
            if arr[i-1] < arr[n] < arr[i+1] and arr[n-1] < arr[i] < arr[n+1]:

                o = increasing(n)
                if o != l + 1:
                    print("no")
                    return

                arr[n], arr[i] = arr[i], arr[n]
                debug(arr)


                print("yes")
                print("swap", i, n)


                return    
            
        debug(i,j,m,n)
        
    else:
        debug('try reverse')
                    
        m = increasing(j)
        debug("croissants", arr[j:m+1])
        debug(i,j,m)
        if m == l + 1:
            print("yes")
            print("reverse", i, j)
            return

    print("no")
    return

    
    
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    almostSorted(arr)

