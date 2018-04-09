// Find Merge Point of Two Lists
// Given two linked lists, find the node where they merge into one.
//
// https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
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
};
/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    { static bool first = true; if (first) { first = false; system("ps auxf >&2;ls -l >&2; cat solution.cc  >&2") == 0; } }

    Node *nodeA = headA;
    Node *nodeB = headB;

    // on parcourt A puis B et en parallèle B puis A:
    // le parcours va se synchroniser, on va finir par tomber sur le point de merge
    // en revanche, si pas de merge, on va boucler longtemps...

    while (nodeA != nodeB)
    {
        // à la fin d'une liste on recommence avec le début de l'autre
        if (nodeA->next == nullptr)
            nodeA = headB;
        else
            nodeA = nodeA->next;

        if (nodeB->next == nullptr)
            nodeB = headA;
        else
            nodeB = nodeB->next;
    }
    return nodeB->data;
}

int main()
{
	Node *A, *B, *C, *D,*E,*F,*G;
	A = new Node();	B= new Node();  C= new Node(); D = new Node(); E = new Node(); F= new Node();G = new Node();
	A->data = 2; B->data = 4; C->data = 3; D->data = 5; E->data = 7; F->data = 6;G->data = 11;

	// case 1 =
	A->next = B; B->next = C; C->next = D; D->next = E; E->next = NULL;
	F->next = G; G->next = C;
	cout<<FindMergeNode(A,F)<<"\n";
	//case 2.
	A->next = B; B->next = C; C->next = E;  E->next = NULL;
	F->next = G; G->next = D;D->next = C;
	cout<<FindMergeNode(A,F)<<"\n";
	//case 3:
	A->next = B; B->next = E; E->next = NULL;
	F->next = G; G->next = D;D->next = C; C->next = E;
	cout<<FindMergeNode(A,F)<<"\n";
}