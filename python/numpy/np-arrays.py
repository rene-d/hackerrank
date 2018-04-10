# Arrays
# Convert a list to an array using the NumPy package. 
# 
# https://www.hackerrank.com/challenges/np-arrays/problem
# 

import numpy
# (template_head) ----------------------------------------------------------------------


def arrays(arr):
    # complete this function
    # use numpy.array 
    arr.reverse()
    return numpy.array(arr, float)


# (template_tail) ----------------------------------------------------------------------
arr = input().strip().split(' ')
result = arrays(arr)
print(result)