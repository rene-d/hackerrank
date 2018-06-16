# Python > Debugging > Default Arguments
# Debug a function which uses a default value for one of its arguments.
#
# https://www.hackerrank.com/challenges/default-arguments/problem
# challenge id: 66403
#

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
# (skeliton_head) ----------------------------------------------------------------------

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

# probable error of author during conversion from Python2 to Python3...
raw_input = input

# (skeliton_tail) ----------------------------------------------------------------------
queries = int(input())
for _ in range(queries):
    stream_name, n = raw_input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
