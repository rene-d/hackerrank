# The Hurdle Race
# Can you help Dan determine the minimum number of magic beverages he must drink to jump all the hurdles?
#
# https://www.hackerrank.com/challenges/the-hurdle-race/problem
#

def hurdleRace(k, height):
    # Complete this function
    return max(0, max(height) - k)


if __name__ == "__main__":
    n, k = map(int, input().split())
    height = list(map(int, input().split(' ')))
    result = hurdleRace(k, height)
    print(result)
