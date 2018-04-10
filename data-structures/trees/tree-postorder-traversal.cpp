// Tree: Postorder Traversal
// Print the post order traversal of a binary tree.
//
// https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
//

#include  "tree.hpp"
MAIN(postOrder)

/* you only have to complete the function given below.
Node is defined as

struct node
{
    int data;
    node* left;
    node* right;
};

*/

// affiche les éléments child avant le noeud courant
void postOrder(node *root)
{
    if (root)
    {
        postOrder(root->left);
        postOrder(root->right);
        cout << root->data << " ";
    }
}
