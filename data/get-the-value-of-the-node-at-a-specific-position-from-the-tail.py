# Get Node Value
# Given the head of a linked list, get the value of the node at a given position when counting backwards from the tail.
#
# https://www.hackerrank.com/contests/master/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
#

#Head
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, node, data):
        new_node = Node(data, node.next)
        node.next = new_node
        if self.tail == node:
            self.tail = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.insert(self.tail, data)
#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    node1 = head
    node2 = head
    i = 0
    while node1 is not None:
        node1 = node1.next
        if i > position:
            node2 = node2.next
        i += 1
    return node2.data

#Tail
if __name__ == "__main__":

    #This will insert the problem setter's linkedlist
    for _ in range(int(input())):
        x1 = int(input())
        y1 = list(map(int,input().split()))

        L1 = LinkedList()
        for i in range(x1):
            L1.insert_end(y1[i])

        print(GetNode(L1.head, int(input())))
