# Tutorials > 30 Days of Code > Day 14: Scope
# Learn about the scope of an identifier.
#
# https://www.hackerrank.com/challenges/30-scope/problem
#

class Difference:
    def __init__(self, a):
        self.__elements = a
# (skeliton_head) ----------------------------------------------------------------------

    def __init__(self, a):
        self.a = a

    def computeDifference(self):
        self.maximumDifference = max(self.a) - min(self.a)

# (skeliton_tail) ----------------------------------------------------------------------
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
