// Reverse a linked list
// Change the links between the nodes of a linked list to reverse it
//
// https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
//

#include "linked-list.hpp"

Node* Reverse(Node *head);

int main()
{
    int t;
    std::cin >> t;
    while (t--)
    {
        std::vector<int> v1, v2;
        Node *a = read_nodes();

        v1 << a;
        std::reverse(v1.begin(), v1.end());

        a = Reverse(a);

        v2 << a;
        if (v1 == v2)
            std::cout << "Right Answer!" << std::endl;
        else
            std::cout << "Wrong Answer!" << std::endl;

        free_nodes(a);
    }

    return 0;
}


/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method

    if (head == NULL) return NULL;
    if (head->next == NULL) return head;

    Node *node, *prev = NULL, *old;

    while (head)
    {
        node = new Node;
        node->data = head->data;
        node->next = prev;

        prev = node;
        old = head;
        head = head->next;
        delete old;
    }

    return node;
}
