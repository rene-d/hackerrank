// Insert a Node at the Tail of a Linked List
// Create and insert a new node at the tail of a linked list.
//
// https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
//

#include "linked-list.hpp"

Node* Insert(Node *head, int data);

int main()
{
    int t, data;
    std::string result;
    Node *a = NULL;
    std::cin >> t;
    while (t--)
    {
        std::cin >> data;
        a = Insert(a, data);
        result += std::to_string(data);
    }
    if (to_str_nodes(a) == result)
        std::cout << "Right Answer!" << std::endl;
    free_nodes(a);

    return 0;
}



/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head, int data)
{
  // Complete this method
    if (head == NULL)
    {
        Node *node= new Node();
        node->data = data;
        node->next = NULL;
        return node;
    }
    for (Node *node = head; ; node = node->next)
    {
        if (node->next == NULL)
        {
            node->next = new Node;
            node->next->data = data;
            node->next->next = NULL;
            return head;
        }
    }
}
