# Repeated String
# Find and print the number of letter a's in the first n letters of an infinitely large periodic string.
#
# https://www.hackerrank.com/challenges/repeated-string/problem
#

def repeatedString(s, n):
    # Complete this function
    q, r = divmod(n, len(s))

    # répétitions de la chaine entière
    nb = q * sum(1 for c in s if c == 'a')

    # la portion de la chaine qui reste pour atteindre les n lettres
    nb += sum(1 for c in s[0:r] if c == 'a')

    return nb


if __name__ == "__main__":
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
