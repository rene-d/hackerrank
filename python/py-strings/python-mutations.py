# Python > Strings > Mutations
# Understand immutable vs mutable by making changes to a given string.
#
# https://www.hackerrank.com/challenges/python-mutations/problem
#

def mutate_string(string, position, character):

    return string[:position] + character + string[position + 1:]


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
