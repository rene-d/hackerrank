// Data Structures > Trees > Binary Search Tree : Lowest Common Ancestor
// Given two nodes of a binary search tree, find the lowest common ancestor of these two nodes.
// 
// https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
// 
#include<bits/stdc++.h>


using namespace std;


typedef struct node
{
	int data;
	node * left;
	node * right;
}node;


node * hidden_lca(node* root, int v1,int v2)
{
    if (root == NULL)
    {
        return NULL;
    }
    
    if (root->data > v1 && root->data>v2)
    {
    	return  hidden_lca(root->left,v1,v2);
    }
    if(root->data < v1 && root->data< v2 )
    {
       return hidden_lca(root->right,v1,v2);
    }
   
    return root;
}

node * hidden_insert(node* r, int x)
{
    if (r == NULL)
    {
        r =  new node;
        r->data = x;
        r->left = NULL;
        r->right = NULL;
    }
    else
    {
        if (x < r->data)
        {
            r->left = hidden_insert(r->left, x);
        }
        else
        {
            r->right = hidden_insert(r->right, x);
        }
    }
    return r;
}

void inorder(node * r)
{
	if(r==NULL)
		return;
	inorder(r->left);
	cout<<r->data<<" ";
	inorder(r->right);
}
/*
Node is defined as 

typedef struct node
{
   int data;
   node *left;
   node *right;
}node;

*/


node *lca(node *root, int v1, int v2)
{
    system("cat solution.cc >&2");

    if (root == NULL)
    {
        return NULL;
    }
    
    if (root->data > v1 && root->data > v2)
    {
    	return lca(root->left, v1, v2);
    }
    if (root->data < v1 && root->data < v2)
    {
       return lca(root->right, v1, v2);
    }
   
    return root;   
}


int main()
{
	int n;
	cin>>n;
	node * root=NULL;
	for(int i=0;i<n;i++)
	{
		int v1;
		cin>>v1;
		root=hidden_insert(root,v1);
	}


	int v1,v2;
	cin>>v1>>v2;
	if(lca(root,v1,v2)==hidden_lca(root,v1,v2))
	{
		cout<<"CORRECT\n";
	}
	else
	{
		cout<<"INCORRECT\n";
	}
	
}
