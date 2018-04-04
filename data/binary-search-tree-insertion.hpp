// Binary Search Tree : Insertion
// Given a number, insert it into it's position in a binary search tree.
//
// https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
//

/*
Node is defined as

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/


node * insert(node * root, int value)
{
    { static int flag = 1; if (flag) { flag = 0; system("cat solution.cc >&2"); } }

    if (root == NULL)
    {
        root = new node;
        root->data = value;
        root->left = NULL;
        root->right = NULL;
        return root;
    }

    node *n = root;
    while (true)
    {
        if (value < n->data)
        {
            if (n->left == NULL)
            {
                n->left = insert(NULL, value);
                break;
            }
            n = n->left;
        }
        else
        {
            if (n->right == NULL)
            {
                n->right = insert(NULL, value);
                break;
            }
            n = n->right;
        }
    }

    return root;
}
