// Insert a node at a specific position in a linked list
// Insert a node at a specific position in a linked list.
//
// https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
//

#include "linked-list.hpp"

Node* InsertNth(Node *head, int data, int position);

int main()
{
    int t, data, position;
    Node *a = NULL;
    std::cin >> t;
    while (t--)
    {
        std::cin >> data >> position;
        a = InsertNth(a, data, position);
    }
    print_nodes(a, "");
    free_nodes(a);

    return 0;
}



/*
  Insert Node at a given position in a linked list
  head can be NULL
  First element in the linked list is at position 0
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
  // Complete this method only
  // Do not write main function.

    if (head == NULL || position == 0)
    {
        Node *node = new Node;
        node->data = data;
        node->next = head;
        return node;
    }

    Node *node = head;
    Node *prev;

    while (position != 0 && node != NULL)
    {
        --position;
        prev = node;
        node = node->next;
    }

    node = new Node;
    node->data = data;
    node->next = prev->next;
    prev->next = node;

    return head;
}
