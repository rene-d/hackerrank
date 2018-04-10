# What's Your Name?
# Python string practice: Print your name in the console.
#
# https://www.hackerrank.com/challenges/whats-your-name/problem
#

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
