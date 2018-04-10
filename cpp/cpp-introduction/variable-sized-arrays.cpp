// Variable Sized Arrays
// Find the element described in the query for integer sequences.
// 
// https://www.hackerrank.com/challenges/variable-sized-arrays/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    vector<vector<int>> w;
    int n, q;
    
    cin >> n >> q;
    while (n-- != 0)
    {
        size_t k; 
        int x;
        vector<int> v;
        
        cin >> k;
        while (k-- != 0) { cin >> x; v.push_back(x); }
        
        w.push_back(v);
    }
    while (q-- != 0)
    {
        size_t i, j;
        cin >> i >> j;    
        cout << w[i][j] << endl;
    }
    return 0;
}

