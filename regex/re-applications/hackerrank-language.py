# Regex > Applications > HackerRank Language
# Use regex if an api request has a valid language string set or not
#
# https://www.hackerrank.com/challenges/hackerrank-language/problem
# https://www.hackerrank.com/contests/regex-practice-2/challenges/hackerrank-language
# challenge id: 715
#

L = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(':')

for _ in range(int(input())):
    ok = input().split()[1].upper() in L
    print("VALID" if ok else "INVALID")
