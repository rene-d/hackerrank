// Security > Functions > Security Involution
// Determine whether function f is an involution or not.
//
// https://www.hackerrank.com/challenges/security-involution/problem
//


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    unsigned int n;
    vector<unsigned int> f;

    cin >> n;
    f.resize(n + 1);
    for (unsigned int i = 1; i <= n; ++i)
    {
        cin >> f[i];
    }

    unsigned int i;
    for (i = 1; i <= n; ++i)
    {
        if (f[f[i]] != i) break;
    }
    cout << ((i == n+1) ? "YES" : "NO");


    return 0;
}
