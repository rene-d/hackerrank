// Merge two sorted linked lists
// Given the heads of two sorted linked lists, change their links to get a single, sorted linked list.
//
// https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
//

#include "linked-list.hpp"

Node* MergeLists(Node *headA, Node* headB);

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        Node *a = read_nodes();
        Node *b = read_nodes();

        Node *m = MergeLists(a, b);

        print_nodes(m);

        free_nodes(m);
        free_nodes(a);
        free_nodes(b);
    }

    return 0;
}

///////////////////////////////////////////////////////////////////////////////
// challenge solution begins here
///////////////////////////////////////////////////////////////////////////////



/*
  Merge two sorted lists A and B as one linked list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission.
  // You only need to complete this method

    if (headA == NULL && headB == NULL) return NULL;

    Node *headC = NULL;
    Node *node = NULL;
    Node *prev = NULL;

    while (headA != NULL || headB != NULL)
    {
        node = new Node;

        if (prev != NULL)
        {
            prev->next = node;
        }
        else
        {
            headC = node;
        }
        prev = node;

        if (headA != NULL && headB != NULL)
        {
            if (headA->data < headB->data)
            {
                node->data = headA->data;
                headA = headA->next;
            }
            else
            {
                node->data = headB->data;
                headB = headB->next;
            }
        }
        else if (headA != NULL)
        {
            node->data = headA->data;
            headA = headA->next;
        }
        else
        {
            node->data = headB->data;
            headB = headB->next;
        }
    }

    // gcc 4.8.4 ne "voit" pas que le while est toujours exécuté, et renvoie un warning -Wmaybe-uninitialized
    // les versions plus récentes et clang sont plus intelligentes !
    if (node != NULL)
        node->next = NULL;

    return headC;
}
