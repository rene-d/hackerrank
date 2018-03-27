# Service Lane
# Calculate the maximum width of the vehicle that can pass through a service lane.
#
# https://www.hackerrank.com/challenges/service-lane/problem
#


def serviceLane(width, a, b):
    # euh? comment dire...
    print(min(width[a:b + 1]))

if __name__ == "__main__":
    n, t = map(int, input().split())
    width = list(map(int, input().split()))
    for _ in range(t):
        a, b = map(int, input().split())
        serviceLane(width, a, b)
