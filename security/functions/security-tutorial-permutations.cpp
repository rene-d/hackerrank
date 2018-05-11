// Security > Functions > Security Permutations
// Given a function f, find f(f(x)) for all x ∈ {1,2,3,...,n}.
// 
// https://www.hackerrank.com/challenges/security-tutorial-permutations/problem
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
    for (int i = 0; i < n; ++i)
    {
        cin >> x;
        f[i] = x;
    }
    
    for (int i = 0; i < n; ++i)
    {
        // attention à l'indexation de f()
        cout << f[f[i] - 1] << endl;
    }
    
        
    return 0;
}

