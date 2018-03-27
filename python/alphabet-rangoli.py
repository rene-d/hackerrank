# Alphabet Rangoli
# Let's draw rangoli.
# 
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# 

def print_rangoli(size):
    # your code goes here

    size -= 1    
    for y in range(-size, size + 1):
        s = ''
        for x in range(-size * 2, size * 2 + 1):
            if x % 2 == 0 and abs(x // 2) <= size - abs(y):
                s += chr(97 + abs(x // 2) + abs(y))
            else:
                s += '-'
        print(s)          


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
