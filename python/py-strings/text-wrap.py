# Python > Strings > Text Wrap
# Wrap the given text in a fixed width.
#
# https://www.hackerrank.com/challenges/text-wrap/problem
#

import textwrap
# (skeliton_head) ----------------------------------------------------------------------

def wrap(string, max_width):
    return "\n".join(string[i:i + max_width] for i in range(0, len(string), max_width))

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
