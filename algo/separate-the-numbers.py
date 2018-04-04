# Separate the Numbers
#   Determine if a numeric string can be broken into a sequence of increasing numbers.
#
# https://www.hackerrank.com/challenges/separate-the-numbers/problem
#

import sys

# cas un peu complexe, il faut bien gérer ses compteurs

def separateNumbers(s):
    # Complete this function
    for i in range(1, len(s) // 2 + 1):
        j = i
        k = 0
        prev = -1
        ugly = False
        # print("test", i,file=sys.stderr)

        while k + j <= len(s):

            # règle n°2
            if s[k] == "0" and j > 1:
                ugly = True
                break

            n = int(s[k:k + j])

            # print("prev=",prev,"n=",n,"j=",j,file=sys.stderr)

            if prev != -1:
                if n != prev + 1:
                    j += 1
                    n = int(s[k:k + j])

                    # règle n°1
                    if n != prev + 1:
                        ugly = True
                        break

            prev = n
            k += j

        if not ugly and k == len(s):
            # print("k=",k,"j=",j,"len(s)=",len(s),file=sys.stderr)
            print("YES", s[0:i])
            return

    print("NO")


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separateNumbers(s)
