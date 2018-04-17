// Tutorials > 30 Days of Code > Day 23: BST Level-Order Traversal
// Implement a breadth-first search!
//
// https://www.hackerrank.com/challenges/30-binary-trees/problem
//

#include <iostream>
#include <cstddef>
#include <queue>
#include <string>
#include <cstdlib>

using namespace std;
class Node{
    public:
        int data;
        Node *left,*right;
        Node(int d){
            data=d;
            left=right=NULL;
        }
};
class Solution{
    public:
  		Node* insert(Node* root, int data){
            if(root==NULL){
                return new Node(data);
            }
            else{
                Node* cur;
                if(data<=root->data){
                    cur=insert(root->left,data);
                    root->left=cur;
                }
                else{
                   cur=insert(root->right,data);
                   root->right=cur;
                 }
           return root;
           }
        }
// (skeliton_head) ----------------------------------------------------------------------

    void levelOrder(Node * root)
    {
        queue<Node *>   q;

        q.push(root);
        while (! q.empty())
        {
            auto n = q.front();
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

// (skeliton_tail) ----------------------------------------------------------------------
};//End of Solution
int main(){
    Solution myTree;
    Node* root=NULL;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        root= myTree.insert(root,data);
    }
    myTree.levelOrder(root);
    return 0;
}
