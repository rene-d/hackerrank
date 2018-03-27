# Compress the String! 
#  groupby()
# 
# https://www.hackerrank.com/challenges/compress-the-string/problem
# 

import itertools

s = input()

print(' '.join(str((len(list(g)), int(c))) 
               for c, g in itertools.groupby(s)))
