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

        float_pattern = re.compile(r'^(\d+\.\d{' + str(DECIMALS) + r'})\d*$')
        zero_pattern = re.compile(r'(\d+)\.0*')

        n = 0
        for i, j in itertools.zip_longest(f, g, fillvalue=''):
            n += 1

            # ignore line endings
            i = i.strip()
            j = j.strip()

            # when a decimal number is found, truncate unwanted digits
            i = float_pattern.sub(r'\1', i)
            j = float_pattern.sub(r'\1', j)

            # remove 0 decimals
            i = zero_pattern.sub(r'\1', i)
            j = zero_pattern.sub(r'\1', j)

            if i.strip() != j.strip():
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
