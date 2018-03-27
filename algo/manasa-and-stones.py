# Manasa and Stones
# Calculate the possible values of the last stone where consecutive values on the stones differ by a value 'a' or a value 'b'.
#
# https://www.hackerrank.com/challenges/manasa-and-stones/problem
#

def stones(n, a, b):
    # si a==b une seule valeur possible
    if a == b:
        return [(n - 1) * a]
    r = []
    if a > b: a, b = b, a

    # sinon c'est l'ensemble de a+a+a+...+b+b (n termes)
    for i in range(n):
        r.append(a * (n - 1 - i) + b * i)
    return r

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print (" ".join(map(str, result)))
