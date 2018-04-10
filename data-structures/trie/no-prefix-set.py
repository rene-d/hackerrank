# No Prefix Set
# Given N strings, find if a string is a prefix of another string.
#
# https://www.hackerrank.com/challenges/no-prefix-set/problem
#

import bisect

def main():
    arr = []

    for _ in range(int(input())):
        s = input()

        p = bisect.bisect_right(arr, s)

        if p >= 1 and s.startswith(arr[p - 1]):
            print("BAD SET")
            print(s)
            return

        if p < len(arr) and arr[p].startswith(s):
            print("BAD SET")
            print(s)
            return

        arr.insert(p, s)

    print("GOOD SET")

main()
