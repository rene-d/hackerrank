"""
Time Delta

https://www.hackerrank.com/challenges/python-time-delta/problem
"""

import sys
import datetime


def to_date(t):
    # Sun 10 May 2015 13:54:36 -0700
    t = datetime.datetime.strptime(t, "%a %d %b %Y %H:%M:%S %z")
    return t
    

def time_delta(t1, t2):
    # Complete this function
    delta = to_date(t1) - to_date(t2)
    return abs(int(delta.total_seconds()))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
