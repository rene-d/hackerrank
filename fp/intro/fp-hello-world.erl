% Hello World
% Write code to print the 'Hello World' program.
%
% https://www.hackerrank.com/challenges/fp-hello-world/problem
%

% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

hello() ->
    io:fwrite("Hello World\n").

main() ->
    hello().
