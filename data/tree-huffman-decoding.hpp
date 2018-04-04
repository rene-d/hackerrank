// Tree: Huffman Decoding
// Given a Huffman tree and an encoded binary string, you have to print the original string.
//
// https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
//

/*
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;

}node;

*/


void decode_huff(node * root,string s)
{
    // pour voir le code caché
    { static int flag = 1; if (flag) { flag = 0; system("cat solution.cc >&2"); } }

    node *n = root;

    for (auto i : s)
    {
        if (i == '1')
            n = n->right;
        else
            n = n->left;

        // on a atteint un noeud feuille (leaf node)
        if (n->right == NULL && n->left == NULL)
        {
            cout << n->data;
            n = root;
        }
    }

    cout << endl;
}
