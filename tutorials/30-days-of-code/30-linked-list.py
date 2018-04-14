# Tutorials > 30 Days of Code > Day 15: Linked List
# Complete the body of a function that adds a new node to the tail of a Linked List.
#
# https://www.hackerrank.com/challenges/30-linked-list/problem
#

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
# (skeliton_head) ----------------------------------------------------------------------

    def insert(self,head,data):
        #Complete this method

        if head is None:
            return Node(data)
        node = head
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        return head

# (skeliton_tail) ----------------------------------------------------------------------
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
