# Balanced Brackets
# Given a string containing three types of brackets, determine if it is balanced.
#
# https://www.hackerrank.com/challenges/balanced-brackets/problem
#

def isBalanced(s):
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if len(stack) == 0:
                return False
            d = stack.pop()
            if d + c not in "(){}[]":
                return False
    return len(stack) == 0


for a0 in range(int(input())):
    s = input()
    print("YES" if isBalanced(s) else "NO")
