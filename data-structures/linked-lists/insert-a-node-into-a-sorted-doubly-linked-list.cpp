// Inserting a Node Into a Sorted Doubly Linked List
// Create a node with a given value and insert it into a sorted doubly-linked list
//
// https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
//
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
using namespace std;
struct Node
{
  int data;
  Node* next;
  Node* prev;
};

//---------------------------------------------------------------------------------------------------

/*
    Insert Node in a doubly sorted linked list
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/

Node* SortedInsert(Node *head,int data)
{
///  { static bool first = true; if (first) { first = false; system("cat solution.cc >&2") == 0; } }

    // Complete this function
   // Do not write the main method.

    Node *nouv;

    nouv = new Node;
    nouv->next = nullptr;
    nouv->prev = nullptr;
    nouv->data = data;


    if (head == NULL)
    {
        return nouv;
    }

    if (data < head->data)
    {
        nouv->next = head;
        head->prev = nouv;
        return nouv;
    }

    Node *node = head;

    for (node = head; node->next != nullptr && node->next->data < data; node = node->next);

    if (node->next != nullptr)
    {
        nouv->next = node->next;
        node->next->prev = nouv;
    }

    node->next = nouv;
    nouv->prev = node;

    return head;
}
//---------------------------------------------------------------------------------------------------


Node * SortedInsertHidden(Node * head, int data)
{
      Node *current = NULL;
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->data=data;
    new_node->next=NULL;
    new_node->prev=NULL;

  if (head == NULL )
  {
    head = new_node;
  }
  else if(head->data >= new_node->data)
  {
    new_node->next = head;
    head->prev=new_node;
    head = new_node;
  }
  else
  {

    current = head;
    while (current->next!=NULL && current->next->data < new_node->data)
    {
      current = current->next;
    }

      if(current->next!=NULL)
      {
          new_node->next = current->next;
          current->next->prev=new_node;
      }
      current->next = new_node;
      new_node->prev=current;

  }
    return head;
}
void Print(Node *head) {
  if(head == NULL) return;
  while(head->next != NULL){ cout<<head->data<<" "; head = head->next;}
  cout<<head->data<<" ";
  while(head->prev != NULL) { cout<<head->data<<" "; head = head->prev; }
  cout<<head->data<<"\n";
}

int checker(Node * head1 , Node * head2)
{
    if(head1==NULL && head2==NULL)return 1;
    if(head1==NULL)return 0;
    if(head2==NULL) return 0;

    if(head1->data!=head2->data)
        return false;

     return checker(head1->next,head2->next);


}

int main()
{
  int t; cin>>t;
  Node *head = NULL;
  Node * head2=NULL;
  string S="Some possible errors:\n1. You returned a NULL value from the function. \n2. There is a problem with your logic";


  while(t--) {
     int n; cin>>n;
           head = NULL;
           head2  = NULL;
     for(int i = 0;i<n;i++) {
       int x; cin>>x;
       head = SortedInsert(head,x);
       head2=SortedInsertHidden(head2,x);

     }
     if(checker(head,head2)==1)
        {
            cout<<"Right Answer!\n";
        }
        else
        {

            cout<<"Wrong Answer!\n";
            cout<<S<<endl;
        }
  }
}