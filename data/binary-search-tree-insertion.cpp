#include<bits/stdc++.h>


using namespace std;


typedef struct node
{
	int data;
	node * left;
	node * right;
}node;

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

void inorder_hidden(node * r)
{
	if(r==NULL)
		return;
	inorder_hidden(r->left);
	cout<<r->data<<" ";
	inorder_hidden(r->right);
}

#include "binary-search-tree-insertion.hpp"

bool check(node * root1,node * root2)
{
	if(root1==NULL && root2==NULL)
		return true;
	if(root1==NULL)
		return false;
	if(root2==NULL)
		return false;

	if(root1->data!=root2->data)
		return false;

	return (check(root1->left,root2->left) && check(root1->right,root2->right));

}

int main()
{
	int n;
	cin>>n;
	node * root=NULL;
	node * root2=NULL;

	for(int i=0;i<n;i++)
	{
		int v1;
		cin>>v1;
		root=hidden_insert(root,v1);
		root2=hidden_insert(root2,v1);

	}


	int ins_value;
	cin>>ins_value;

	root=insert(root,ins_value);
	root2=hidden_insert(root2,ins_value);
	string S="Some possible errors:\n1. You returned a NULL value from the function. \n2. There is a problem with your logic\n3. You are printing some value from the function ";


	if(check(root,root2))
	{
		cout<<"Right Answer!\n";
	}
	else
	{
		cout<<"Wrong Answer!\n";
		cout<<S<<endl;
	}
	//norder_hidden(root);
	//cout<<endl;

}