# Queue using Two Stacks
# Create a queue data structure using two stacks.
#
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
#

in_stack = []
out_stack = []

for _ in range(int(input())):
    op = list(map(int, input().split()))

    # push back
    if op[0] == 1:
        in_stack.append(op[1])

    # pop front
    elif op[0] == 2:
        if len(out_stack) > 0:
            # vide la stack de sortie
            out_stack.pop()
        else:
            # transvase la stack d'entrée vers la stack de sortie
            while len(in_stack) > 1:
                out_stack.append(in_stack.pop())
            in_stack.pop()

    # print
    elif op[0] == 3:
        if len(out_stack) == 0:
            while len(in_stack) > 0:
                out_stack.append(in_stack.pop())
        print(out_stack[-1])
