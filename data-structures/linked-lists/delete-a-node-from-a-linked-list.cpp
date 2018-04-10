// Delete a Node
// Delete a node from the linked list and return the head.
//
// https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
//


#include "linked-list.hpp"

Node* Delete(Node *head, int position);

int main()
{
    int t, position;
    std::cin >> t;
    while (t--)
    {
        Node *a = read_nodes();
        std::cin >> position;
        a = Delete(a, position);
        print_nodes(a, "");
        free_nodes(a);
    }

    return 0;
}




/*
  Delete Node at a given position in a linked list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
  // Complete this method
    if (head == NULL) return NULL;
    if (position == 0)
    {
        Node *node = head->next;
        delete head;
        return node;
    }

    Node *node = head;
    Node *prev;
    while (position != 0 && node)
    {
        --position;
        prev = node;
        node = node->next;
    }

    if (node != NULL)
    {
        prev->next = node->next;
        delete node;
    }

    return head;
}
