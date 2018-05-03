#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Compare a HackerRank testcase result fairly with decimal numbers,
taking into account up to DECIMALS digits (and ignoring the following).
"""

from __future__ import print_function
import sys
import re
import itertools


DECIMALS = 5


def main():
    if len(sys.argv) != 3:
        print("Usage: compare.py file1 file2")
        sys.exit(2)

    try:
        f = open(sys.argv[1], "r")
        g = open(sys.argv[2], "r")

        float_pattern = re.compile(r'(\d+\.)(\d+)')

        def float_fmt(m):
            return m.group(1) + m.group(2)[:DECIMALS].ljust(DECIMALS, "0")

        n = 0
        for i, j in itertools.zip_longest(f, g, fillvalue=''):
            n += 1

            # ignore line endings
            i = i.rstrip()
            j = j.rstrip()

            # when a float number is found, adjust decimal digits
            i = float_pattern.sub(float_fmt, i)
            j = float_pattern.sub(float_fmt, j)

            if i != j:
                # a difference is found
                print('{}< {}'.format(n, i))
                print('{}> {}'.format(n, j))
                sys.exit(1)

        # everything's fine!
        sys.exit(0)

    except Exception as f:
        print(f, file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
