"""
Capitalize!

https://www.hackerrank.com/challenges/capitalize/problem
"""

def capitalize(string):
    s = ""
    for i in range(len(string)):
        if i == 0 or string[i-1] == ' ':
            s += string[i].upper()
        else:
            s += string[i]
    return s

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
