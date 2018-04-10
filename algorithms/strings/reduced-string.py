# Super Reduced String
# Given a string, repeatedly remove adjacent pairs of matching characters and then print the reduced result.
# 
# https://www.hackerrank.com/challenges/reduced-string/problem
# 

def super_reduced_string(s):
    # Complete this function
    l = len(s)
    i = 0
    r = ""
    while i < l - 1:
        if s[i] == s[i + 1]:
            i += 2
        else:
            if len(r) != 0 and r[-1] == s[i]:
                r = r[:-1]
            else:
                r += s[i]
            i += 1
    if i == l - 1:
        if len(r) != 0 and r[-1] == s[l - 1]:
            r = r[:-1]
        else:
            r += s[l - 1]
    if r == "":
        r = "Empty String"
    return r
    
s = input().strip()
result = super_reduced_string(s)
print(result)
