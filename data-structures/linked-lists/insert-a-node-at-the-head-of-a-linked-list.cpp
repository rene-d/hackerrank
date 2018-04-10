// Insert a node at the head of a linked list
// Create and insert a new node at the head of a linked list
//
// https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
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
        result = std::to_string(data) + result;
    }
    if (to_str_nodes(a) == result)
        std::cout << "Right Answer!" << std::endl;
    free_nodes(a);

    return 0;
}


/*
  Insert Node at the begining of a linked list
  Initially head pointer argument could be NULL for empty list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
return back the pointer to the head of the linked list in the below method.
*/
Node* Insert(Node *head, int data)
{
  // Complete this method
    Node *node = new Node;
    node->data = data;
    node->next = head;
    return node;
}
