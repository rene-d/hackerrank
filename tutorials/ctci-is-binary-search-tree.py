# Trees: Is This a Binary Search Tree?
# Given the root of a binary tree, determine if it's a binary search tree.
#
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
#

# code caché obtenu avec:
# import os
# os.system("cat solution.py >&2")


#------------------------------------------------------------------------------
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode():
    temp =  node(-1)
    temp.left = None
    temp.right = None

    return(temp);
#------------------------------------------------------------------------------


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root, min, max):
    return (root is None
            or (min < root.data < max
                and check(root.left, min, root.data)
                and check(root.right, root.data, max)))

def checkBST(root):
    return check(root, 0, 10000)


#------------------------------------------------------------------------------
ht = int(input())
cnt = 0
values = list(map(int, input().split(' ')))
root  = newNode()
def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if(ht>0):
            root.left = newNode();
            inorder(root.left, ht-1);
        root.data = values[cnt];
        cnt += 1
        if ht > 0:
            root.right = newNode();
            inorder(root.right, ht-1);
inorder(root, ht);
if(checkBST(root)):
    print("Yes")
else:
    print("No")
#------------------------------------------------------------------------------
