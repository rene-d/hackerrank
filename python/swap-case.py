# sWAP cASE
# Swap the letter cases of a given string.
#
# https://www.hackerrank.com/challenges/swap-case/problem
#

def swap(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()

def swap_case(s):
    return ''.join([swap(c) for c in s])

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
