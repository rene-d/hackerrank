"""
Time Conversion

https://www.hackerrank.com/challenges/time-conversion/problem
"""

#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    
    if s[-2:] == "AM": 
        # Midnight is 12:00:00AM on a 12-hour clock
        if s[0:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[0:2] == "12":
            # Noon is 12:00:00PM on a 12-hour clock
            return s[:-2]
        else:
            return str(int(s[0:2]) + 12) + s[2:-2]

s = input().strip()
result = timeConversion(s)
print(result)


# https://hr-testcases-us-east-1.s3.amazonaws.com/8649/input01.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1520786241&Signature=aX4vtcdHadsUyNtWQJkKmRgaOh4%3D&response-content-type=text%2Fplain
# https://hr-testcases-us-east-1.s3.amazonaws.com/8649/output01.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1520786253&Signature=SaxZKgqVjMLgK2v%2BHbWTNiogr98%3D&response-content-type=text%2Fplain
