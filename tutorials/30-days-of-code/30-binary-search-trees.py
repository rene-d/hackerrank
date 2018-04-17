# Tutorials > 30 Days of Code > Day 22: Binary Search Trees
# Given a binary tree, print its height.
#
# https://www.hackerrank.com/challenges/30-binary-search-trees/problem
#

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

    def getHeight(self,root,height=0):
        #Write your code here

        h = height
        if root.left is not None:
            h = max(h, self.getHeight(root.left, height + 1))
        if root.right is not None:
            h = max(h, self.getHeight(root.right, height + 1))
        return h

# (skeliton_tail) ----------------------------------------------------------------------
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
