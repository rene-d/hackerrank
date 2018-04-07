# Apple and Orange
# Find the respective numbers of apples and oranges that fall on Sam's house.
#
# https://www.hackerrank.com/challenges/apple-and-orange/problem
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    print(sum(1 for i in apples if s <= (a + i) <= t))
    print(sum(1 for i in oranges if s <= (b + i) <= t))


if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apple = map(int, input().split())
    orange = map(int, input().split())
    countApplesAndOranges(s, t, a, b, apple, orange)
