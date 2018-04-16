# Tree: Height of a Binary Tree
# Given a binary tree, print its height.
#
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
#

class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
# (skeliton_head) ----------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

    def getHeight(self,root,height=0):
        #Write your code here

        h = height
        if root.left is not None:
            h = max(h, self.getHeight(root.left, height + 1))
        if root.right is not None:
            h = max(h, self.getHeight(root.right, height + 1))
        return h


# (skeliton_tail) ----------------------------------------------------------------------
tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))
