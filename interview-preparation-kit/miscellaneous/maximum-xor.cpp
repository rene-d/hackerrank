// Interview Preparation Kit > Miscellaneous > Maximum Xor
// Find the maximum xor value in the array.
//
// https://www.hackerrank.com/challenges/maximum-xor/problem?h_l=playlist&slugs%5B%5D%5B%5D=interview&slugs%5B%5D%5B%5D=interview-preparation-kit&slugs%5B%5D%5B%5D=miscellaneous
// challenge id: 71420
//

#include <bits/stdc++.h>

using namespace std;

// ref: https://www.geeksforgeeks.org/maximum-possible-xor-every-element-array-another-array/

// Structure of Trie DS
struct trie
{
    int value = 0;
    trie *child[2] = { nullptr, nullptr };
};


// Computing maximum xor
int max_xor(trie * root, int key)
{
    trie * temp = root;

    // Checking for all bits in integer range
    for (int i = 31; i >= 0; i--)
    {
        // Current bit in the number
        int current_bit = (key & (1 << i)) ? 1 : 0;

        // Traversing Trie for opposite bit, if found
        if (temp->child[1 - current_bit] != nullptr)
            temp = temp->child[1 - current_bit];

        // Traversing Trie for same bit
        else
            temp = temp->child[current_bit];
    }

    // Returning xor value of maximum bit difference
    // value. Thus, we get maximum xor value
    return (key ^ temp->value);
}

// Inserting A[] in Trie
void insert(trie * root, int key)
{
    trie * temp = root;

    // Storing 32 bits as integer representation
    for (int i = 31; i >= 0; i--)
    {
        // Current bit in the number
        int current_bit = (key & (1 << i)) ? 1 : 0;

        // New node required
        if (temp->child[current_bit] == nullptr)
            temp->child[current_bit] = new trie;

        // Traversing in Trie
        temp = temp->child[current_bit];
    }

    // Assigning value to the leaf node
    temp->value = key;
}

int main()
{
    trie * root = new trie;
    int n, x;

    cin >> n;
    while (n--)
    {
        cin >> x;
        insert(root, x);
    }

    cin >> n;
    while (n--)
    {
        cin >> x;
        cout << max_xor(root, x) << endl;
    }

    return 0;
}


int trivial()
{
    vector<int> A;
    size_t n, t;
    int x, y, m;

    cin >> n;
    A.resize(n);
    for (size_t i = 0; i < n; ++i)
        cin >> A[i];

    cin >> t;
    while (t--)
    {
        cin >> x;

        m = 0;
        for (size_t i = 0; i < n; ++i)
        {
            y = x ^ A[i];
            if (y > m) m = y;
        }
        cout << m << endl;
    }
    return 0;
}
