# Python > Strings > Designer Door Mat
# Print a designer door mat.
#
# https://www.hackerrank.com/challenges/designer-door-mat/problem
#

"""
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""

N, M = map(int, input().split())

s = list((".|." * i).center(M, "-") for i in range(1, N, 2))
print("\n".join(s + ["WELCOME".center(M, "-")] + list(reversed(s))))


#print("\n".join((".|." * i).center(M, "-") for i in range(1, N, 2)))
#print("WELCOME".center(M, "-"))
#print("\n".join((".|." * i).center(M, "-") for i in range(N - 2, -1, -2)))