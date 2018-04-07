# Reverse a doubly linked list
# Given the head node of a doubly linked list, reverse it.
#
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
#
#Head
class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def Insert(head, data):

    n = Node(data)
    if head is None:
        head = n
    else:
        temp = head
        while(temp.next is not None):
            temp = temp.next
        temp.next = n
        n.prev = temp
    return head

def ReverseHidden(head):
    last = head
    current = head.next
    while(current != None):
        nextNode = current.next
        current.next = last
        last.prev = current
        last = current
        current = nextNode
    head.next = None
    return last

def get_list(head):
        temp = head
        s = ""
        while(temp != None):
            s += str(temp.data)+' '
            temp = temp.next
        return s


#import os
#os.system("cat solution.py >&2")

"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""
def Reverse(head):
    node = head
    while node:
        node.next, node.prev = node.prev, node.next
        if node.prev is None: head = node
        node = node.prev
    return head


#Tail
if __name__ == "__main__":

    t = int(input())
    head = Node(0)
    head2 = Node(0)
    S = "Some possible errors:\n1. You returned a None value from the function. \n2. There is a problem with your logic"

    for _ in range(t):
        x = int(input())
        head = Node(0)
        head2 = Node(0)
        if x > 0:
            y = list(map(int, input().split()))
            for i in range(x):
                head = Insert(head,y[i])
                head2 = Insert(head2,y[i])

        a = get_list(ReverseHidden(head))

        b = get_list(Reverse(head2))
        if a == b:
            print("Right Answer!")
        else:
            print("Wrong Answer!")
            print(S)