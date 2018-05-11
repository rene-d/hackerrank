# Algorithms > Sorting > Correctness and the Loop Invariant
# How do you demonstrate the correctness of an algorithm? You can use the loop invariant.
#
# https://www.hackerrank.com/challenges/correctness-invariant/problem
#

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i- 1
        key = l[i]
        while j >= 0 and l[j] > key:
           l[j + 1] = l[j]
           j -= 1
        l[j+1] = key


# (template_tail) ----------------------------------------------------------------------
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
