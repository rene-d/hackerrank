// Tutorials > 30 Days of Code > Day 15: Linked List
// Complete the body of a function that adds a new node to the tail of a Linked List.
//
// https://www.hackerrank.com/challenges/30-linked-list/problem
//

#include <iostream>
#include <cstddef>
using namespace std;
class Node
{
    public:
        int data;
        Node *next;
        Node(int d){
            data=d;
            next=NULL;
        }
};
class Solution{
    public:
// (skeliton_head) ----------------------------------------------------------------------

      Node* insert(Node *head,int data)
      {
          //Complete this method
          if (head == NULL)
          {
            return new Node(data);
          }
          Node *node = head;
          while (node->next)
          {
              node = node->next;
          }
          node->next = new Node(data);
          return head;
      }

// (skeliton_tail) ----------------------------------------------------------------------
void display(Node *head)
      {
          Node *start=head;
          while(start)
          {
              cout<<start->data<<" ";
              start=start->next;
          }
      }
};
int main()
{
	Node* head=NULL;
  	Solution mylist;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        head=mylist.insert(head,data);
    }
	mylist.display(head);

}
