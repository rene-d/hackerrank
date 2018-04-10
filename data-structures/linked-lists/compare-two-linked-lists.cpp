// Compare two linked lists
// Compare the data in two linked lists node by node to see if the lists contain identical data.
//
// https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
//

///////////////////////////////////////////////////////////////////////////////
// main function
///////////////////////////////////////////////////////////////////////////////

#include "linked-list.hpp"

int CompareLists(Node *headA, Node* headB);

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        Node *a = read_nodes();
        Node *b = read_nodes();

        std::cout << CompareLists(a, b) << std::endl;

        free_nodes(a);
        free_nodes(b);
    }

    return 0;
}

///////////////////////////////////////////////////////////////////////////////
// challenge solution begins here
///////////////////////////////////////////////////////////////////////////////


/*
  Compare two linked lists A and B
  Return 1 if they are identical and 0 if they are not.
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int CompareLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission.
  // You only need to complete this method

    while (headA != NULL && headB != NULL && headA->data == headB->data)
    {
        headA = headA->next;
        headB = headB->next;
    }

    return (headA == NULL && headB == NULL) ? 1 : 0;
}
