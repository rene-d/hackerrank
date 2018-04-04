// Tree : Top View
// Given a binary tree, print it's top view.
//
// https://www.hackerrank.com/challenges/tree-top-view/problem
//

#include "tree.hpp"
MAIN(topView)

/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

void topView_left(node * root)
{
    if (root) {
        if (root->left) topView_left(root->left);
        cout << root->data << " ";
    }
}

void topView_right(node * root)
{
    if (root) {
        cout << root-> data << " ";
        if (root->right) topView_right(root->right);
    }
}

void topView(node * root)
{
    if (root) {
        topView_left(root->left);
        cout << root->data << " ";
        topView_right(root->right);
    }
    cout << endl;
}
