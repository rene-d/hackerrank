// Tree: Level Order Traversal
// Level order traversal of a binary tree.
//
// https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
//

#include "tree.hpp"
MAIN(levelOrder)

/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

void levelOrder(node * root)
{
    queue<node *>   q;

    q.push(root);
    while (! q.empty())
    {
        node *n = q.front();
        q.pop();

        if (n)
        {
            cout << n->data << " ";

            q.push(n->left);
            q.push(n->right);
        }
    }

    cout << endl;
}
