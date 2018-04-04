// Tree: Inorder Traversal
// Print the inorder traversal of a binary tree.
//
// https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
//

#include  "tree.hpp"
MAIN(inOrder)

/* you only have to complete the function given below.
Node is defined as

struct node
{
    int data;
    node* left;
    node* right;
};

*/

// affiche left - noeud courant - right
void inOrder(node *root)
{
    if (root)
    {
        inOrder(root->left);
        cout << root->data << " ";
        inOrder(root->right);
    }
}
