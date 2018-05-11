// Security > Functions > Security Function Inverses
// Find the inverse of a given function f.
// 
// https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    int n, x;
    vector<int> f;
    
    cin >> n;
    f.resize(n);
    for (int i = 1; i <= n; ++i)
    {
        cin >> x;
        f[x - 1] = i;
    }
    
    for (auto i : f)
        cout << i << endl;
    
        
    return 0;
}

