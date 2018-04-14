# Python > Strings > String Validators
# Identify the presence of alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters in a string.
#
# https://www.hackerrank.com/challenges/string-validators/problem
#

if __name__ == '__main__':
    s = input()

    # any alphanumeric characters
    print(any(c.isalnum() for c in s))

    # any alphabetical characters
    print(any(c.isalpha() for c in s))

    # any digits
    print(any(c.isdigit() for c in s))

    # any lowercase characters
    print(any(c.islower() for c in s))

    # any uppercase characters
    print(any(c.isupper() for c in s))
