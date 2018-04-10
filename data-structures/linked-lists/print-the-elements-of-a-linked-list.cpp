// Print the Elements of a Linked List
// Get started with Linked Lists!
//
// https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
//

#include "linked-list.hpp"

void Print(Node *head);

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        Node *a = read_nodes();
        Print(a);
        free_nodes(a);
    }

    return 0;
}


/*
  Print elements of a linked list on console
  head pointer input could be NULL as well for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
void Print(Node *head)
{
  // This is a "method-only" submission.
  // You only need to complete this method.
    for (; head; head = head->next)
    {
        std::cout << head->data << std::endl;
    }
}
