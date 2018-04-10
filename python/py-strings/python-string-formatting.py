# String Formatting
# Print the formatted decimal, octal, hexadecimal, and binary values for $n$ integers.
# 
# https://www.hackerrank.com/challenges/python-string-formatting/problem
# 

def print_formatted(number):
    # your code goes here
    
    w = len(bin(number)) - 2    # ne compte pas le préfixe 0b
    for n in range(1, number + 1):
       print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(n, w))


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
