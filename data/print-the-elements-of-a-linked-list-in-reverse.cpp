// Print in Reverse
// Print the elements of a linked list in reverse order, from tail to head
//
// https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
//

#include "linked-list.hpp"

void ReversePrint(Node *head);

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        Node *a = read_nodes();
        ReversePrint(a);
        free_nodes(a);
    }

    return 0;
}



/*
  Print elements of a linked list in reverse order as standard output
  head pointer could be NULL as well for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
void ReversePrint(Node *head)
{
  // This is a "method-only" submission.
  // You only need to complete this method.

    size_t len = 0;
    for (Node *node = head; node; node = node->next) ++len;

    Node **nodes = new Node*[len];
    len = 0;
    for (Node *node = head; node; node = node->next) nodes[len++] = node;

    for (; len; )
    {
        std::cout << nodes[--len]->data << std::endl;
    }

    delete[] nodes;
}
