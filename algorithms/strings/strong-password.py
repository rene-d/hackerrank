# Algorithms > Strings > Strong Password
# How many characters should you add to make the password strong?
#
# https://www.hackerrank.com/challenges/strong-password/problem
#

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


# pseudo strpbrk()
def strpbrk(s1, s2):
    for c in s2:
        if s1.find(c) != -1: return True
    return False


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    k = 0
    if not strpbrk(password, numbers): k += 1
    if not strpbrk(password, lower_case): k += 1
    if not strpbrk(password, upper_case): k += 1
    if not strpbrk(password, special_characters): k += 1
    while n + k < 6: k += 1
    return k


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
