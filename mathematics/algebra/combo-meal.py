# Mathematics > Algebra > Combo Meal
# Find the profit that a fast-food chain earns at each purchase.
#
# https://www.hackerrank.com/challenges/combo-meal/problem
#

def profit(b, s, c):
    # Return the fixed profit.

    # b = b0 + profit
    # s = s0 + profit
    # c = b0 + s0 + profit
    # donc b + s - c = b0 + profit + s0 + profit - (b0 + s0 + profit)
    #                = b0 + profit + s0 + profit - b0 - s0 - profit
    #                = profit

    return b + s - c

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, s, c = input().strip().split(' ')
        b, s, c = [int(b), int(s), int(c)]
        result = profit(b, s, c)
        print(result)
