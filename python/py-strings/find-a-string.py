# Python > Strings > Find a string
# Find the number of occurrences of a substring in a string.
#
# https://www.hackerrank.com/challenges/find-a-string/problem
#

def count_substring(string, sub_string):
    count = 0
    pos = 0
    while True:
        pos = string.find(sub_string, pos)
        if pos == -1:
            break
        pos += 1
        count += 1
    return count


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
