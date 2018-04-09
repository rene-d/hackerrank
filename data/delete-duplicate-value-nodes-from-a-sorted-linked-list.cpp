// Delete duplicate-value nodes from a sorted linked list
// Given a linked list whose nodes have data in ascending order, delete some nodes so that no value occurs more than once.
//
// https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
//

#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
struct Node
{
	int data;
	Node *next;
};

//------------------------------------------------------------------------------------------------
/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
    //{ static bool first = true; if (first) { first = false; system("ps auxf >&2;ls -l >&2; cat solution.cc  >&2") == 0; } }

  // This is a "method-only" submission.
  // You only need to complete this method.

    Node *node = head;

    while (node)
    {
        if (node->next && node->data == node->next->data)
            node->next = node->next->next;
        else
            node = node->next;
    }
    return head;
}
//------------------------------------------------------------------------------------------------

void Print(Node *head)
{
	bool ok = false;
	while(head != NULL)
	{
		if(ok)cout<<" ";
		else ok = true;
		cout<<head->data;
		head = head->next;
	}
	cout<<"\n";
}
Node* Insert(Node *head,int x)
{
   Node *temp = new Node();
   temp->data = x;
   temp->next = NULL;
   if(head == NULL)
   {
       return temp;
   }
   Node *temp1;
   for(temp1 = head;temp1->next!=NULL;temp1= temp1->next);
   temp1->next = temp;return head;
}
int main()
{
	int t;
	cin>>t;
	while(t-- >0)
	{
		Node *A = NULL;
		int m;cin>>m;
		while(m--){
			int x; cin>>x;
			A = Insert(A,x);}
		A = RemoveDuplicates(A);
		Print(A);
	}
}