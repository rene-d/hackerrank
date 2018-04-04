# Day 2: Operators
# Start using arithmetic operators.
#
# https://www.hackerrank.com/challenges/30-operators/problem
#

#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    cost = meal_cost * (1 + tip_percent / 100 + tax_percent / 100)

    print("The total meal cost is {:.0f} dollars.".format(cost))
