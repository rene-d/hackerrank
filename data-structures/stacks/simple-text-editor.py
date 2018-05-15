# Data Structures > Stacks > Simple Text Editor
# Implement a simple text editor and perform some number of operations.
#
# https://www.hackerrank.com/challenges/simple-text-editor/problem
#
import sys

text = ""
undo = []

"""
if t[0]=='1':order+=1;s+=t[1];dic[order]=s
elif t[0]=='2':s=s[:len(s)-int(t[1])];order+=1;dic[order]=s
elif t[0]=='3':print(s[int(t[1])-1])
elif t[0]=='4':order-=1;s=dic[order]
"""

for _ in range(int(input())):
    cmd, _, opt = input().strip().partition(' ')

    avant = text

    if cmd == "1":
        # append s
        undo.append(("append", len(text)))
        text += opt

    elif cmd == "2":
        # delete k
        k = int(opt)
        if k > len(text): k = len(text)
        undo.append(("delete", text[-k:]))
        text = text[:-k]

    elif cmd == "3":
        # print k
        k = int(opt) - 1
        print(text[k])

    elif cmd == "4":
        # undo
        if len(undo) > 0:
            op, opt = undo[-1]
            undo = undo[:-1]

            if op == "append":
                text = text[:opt]
            else:
                text += opt

    # print(">>> {:6} {} {} -> {}".format(['','append','delete','print','undo'][int(cmd)], opt, avant, text), file=sys.stderr)
