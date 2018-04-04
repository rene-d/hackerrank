# Mars Exploration
# Save Our Ship!
#
# https://www.hackerrank.com/challenges/mars-exploration/problem
#


def marsExploration(s):
    # Complete this function
    nb = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c != "SOS"[i % 3]:
            nb += 1
        i += 1
    return nb


if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
