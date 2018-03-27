# Fair Rations
# How many loaves of bread will it take to feed your subjects?
#
# https://www.hackerrank.com/challenges/fair-rations/problem
#

# pas compliqué, le use case donne la solution :)
# on saute les nombres pairs
# il faut donner une miche au premier nombre impair et au suivant
# et on recommence à partir de ce suivant

def fairRations(B):
    loaves = 0
    i = 0
    while i < len(B):
        if B[i] % 2 == 1:
            if i == len(B) - 1:
                return "NO"
            B[i] += 1
            B[i + 1] += 1
            loaves += 2
        i += 1
    return loaves


if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
