# Tutorials > 30 Days of Code > Day 23: BST Level-Order Traversal
# Implement a breadth-first search!
#
# https://www.hackerrank.com/challenges/30-binary-trees/problem
#

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
# (skeliton_head) ----------------------------------------------------------------------

    def levelOrder(self,root):
        queue = []
        result = []

        queue.append(root)
        while queue:
            n = queue.pop(0)
            if n:
                result.append(n.data)
                queue.append(n.left)
                queue.append(n.right)

        print(*result)

# (skeliton_tail) ----------------------------------------------------------------------
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
