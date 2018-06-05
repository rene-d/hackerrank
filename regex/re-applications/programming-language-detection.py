# Regex > Applications > Building a Smart IDE: Programming Language Detection
# You are provided with a set of programs in Java, C and Python and you are also told which of the languages each program is in. Now, given a program written in one of these languages, can you identify which of the languages it is written in?
#
# https://www.hackerrank.com/challenges/programming-language-detection/problem
# challenge id: 672
#

import sys

src = sys.stdin.read()

if '#include' in src:
    print("C")
elif 'import java' in src:
    print("Java")
else:
    print("Python")
