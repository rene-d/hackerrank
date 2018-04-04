// stub pour certains challenges "Data Structures > Trees"
// code caché obtenu avec system("cat solution.cc >&2");

#include<bits/stdc++.h>
using namespace std;

typedef struct node{
    int data;
    struct node *left,*right;
}node;

node* newNode(int val){
    node* tmp = new node();
    tmp->data = val;
    tmp->left = NULL;
    tmp->right = NULL;
    return tmp;
}

node* insert_hidden(node* ptr , int val){

    if(ptr == NULL){
        return newNode(val);
    }
    else if(val > ptr->data)
        ptr->right = insert_hidden(ptr->right , val);
    else if(val < ptr->data)
        ptr->left = insert_hidden(ptr->left , val);
    return ptr;
}

void inorder_hidden(node *ptr){
    if(ptr != NULL){
        inorder_hidden(ptr->left);
        cout<<ptr->data<<" ";
        inorder_hidden(ptr->right);
    }
}


// ajout rené: fonction main() pour appeler la fonction à tester
#define MAIN(fonction) \
    void fonction(node *root);                  \
    int main(){                                 \
        node *root = NULL;                      \
        int n;cin>>n;                           \
        for(int i=0;i<n;i++){                   \
            int val;cin>>val;                   \
            root = insert_hidden(root , val);   \
        }                                       \
        fonction(root);                         \
    }
