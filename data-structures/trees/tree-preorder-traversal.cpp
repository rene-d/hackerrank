// Tree: Preorder Traversal
// Print the preorder traversal of a binary tree.
//
// https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
//

#include  "tree.hpp"
MAIN(preOrder)

/* you only have to complete the function given below.
Node is defined as

struct node
{
    int data;
    node* left;
    node* right;
};

*/

// affiche le noeud courant avant, puis les childs
void preOrder(node *root)
{
    if (root)
    {
        cout << root->data << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}
