// Tutorials > 30 Days of Code > Day 24: More Linked Lists
// Welcome to Day 24! Review everything we've learned so far and learn more about Linked Lists in this challenge.
//
// https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
//

#include <cstddef>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
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

          Node* removeDuplicates(Node *head)
          {
            //Write your code here
              if (head == nullptr) return head;

              Node *node = head;
              while (node->next != nullptr)
              {
                  if (node->data == node->next->data)
                  {
                      Node *old = node->next;
                      node->next = node->next->next;
                      delete old;
                  }
                  else
                  {
                      node = node->next;
                  }
              }

              return head;
          }

// (skeliton_tail) ----------------------------------------------------------------------
Node* insert(Node *head,int data)
          {
               Node* p=new Node(data);
               if(head==NULL){
                   head=p;

               }
               else if(head->next==NULL){
                   head->next=p;

               }
               else{
                   Node *start=head;
                   while(start->next!=NULL){
                       start=start->next;
                   }
                   start->next=p;

               }
                    return head;


          }
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
    head=mylist.removeDuplicates(head);

	mylist.display(head);

}
