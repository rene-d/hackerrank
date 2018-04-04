// Tree: Height of a Binary Tree
// Given a binary tree, print its height.
//
// https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
//

#include <iostream>
#include <cstddef>

using namespace std;

class Node{
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d){
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            }
            else {
                Node* cur;
                if(data <= root->data){
                    cur = insert(root->left, data);
                    root->left = cur;
                }
                else{
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }
// (skeliton_head) ----------------------------------------------------------------------

/*The tree node has data, left child and right child
class Node {
    int data;
    Node* left;
    Node* right;
};

*/

    int height(Node* root, int level = 0)
    {
        int h = level;
        if (root->left) h = std::max(h, height(root->left, level + 1));
        if (root->right) h = std::max(h, height(root->right, level + 1));
        return h;
    }

// (skeliton_tail) ----------------------------------------------------------------------
}; //End of Solution

int main() {
    Solution myTree;
    Node* root = NULL;
    int t;
    int data;

    cin >> t;

    while(t-- > 0){
        cin >> data;
        root = myTree.insert(root, data);
    }
    int height = myTree.height(root);
    cout << height;

    return 0;
}
