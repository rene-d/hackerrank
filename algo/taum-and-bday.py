# Taum and B'day
# Calculate the minimum cost required to buy some amounts of two types of gifts when costs of each type and the rate of conversion from one form to another is provided.
#
# https://www.hackerrank.com/challenges/taum-and-bday/problem
#


def taumBday(b, w, x, y, z):
    # Complete this function

    # x : cost of b
    # y : cost of w
    # z : cost of b <-> w
    return min(x * b + y * w,           # coût avec aucune transformation
               (y + z) * b + y * w,     # coût en transformant b en w
               x * b + (x + z) * w)     # coût en transformant w en b


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print(result)
