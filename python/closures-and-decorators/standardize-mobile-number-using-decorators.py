"""
Standardize Mobile Number Using Decorators

https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""

def wrapper(f):
    def fun(l):
        # complete the function
        for i, n in enumerate(l):
            if len(n) == 10: n= "+91" + n
            elif len(n) == 11 and n.startswith("0"): n = "+91" + n[1:]
            elif len(n) == 12 and n.startswith("91"): n = "+" + n
            elif len(n) == 13 and n.startswith("+91"): pass
            else: continue
            n = n[0:3] + " " + n[3:8] + " " + n[8:] 
            l[i] = n
        return f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
