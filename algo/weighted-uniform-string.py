# Weighted Uniform Strings
# Determine if a string contains uniform substrings of certain weights.
#
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
#

def weightedUniformStrings(s, queries):

    weights = set()
    prev = ''
    w = 0
    for c in s:
        if prev != c:
            prev = c
            w = 0
        w += (ord(c) - ord('a') + 1)
        weights.add(w)

    for q in queries:
        if q in weights:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    weightedUniformStrings(s, queries)
