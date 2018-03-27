"""
Merge the Tools!

https://www.hackerrank.com/challenges/merge-the-tools/problem
"""

def uniq(tableau):
    deja_present = set()
    for element in tableau:
        if element not in deja_present:
            deja_present.add(element)
            yield element


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        tableau = string[i:i + k]
        print(''.join(uniq(tableau)))

        """ équivalent:
        resultat = []
        deja_present = set()
        for element in tableau:
            if element not in deja_present:
                deja_present.add(element)
                resultat.append(element)
        """

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
