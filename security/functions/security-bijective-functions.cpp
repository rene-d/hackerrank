// Security > Functions > Security Bijective Functions
// You'll be given an integer n and a function f:X→X where X={1,2,3,...,n}.  Determine whether the function is a bijective function or not.
// 
// https://www.hackerrank.com/challenges/security-bijective-functions/problem
// 


#include <cmath>
#include <cstdio>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    int n, x;
    set<int> f;
    
    cin >> n;
     
    // pour que f soit bijective, il faut que :
    //  x soit dans [1, n]
    //  l'ensemble des valeurs [1, n] soit couvert => aucun doublon
    for (int i = 0; i < n; ++i)
    {
        cin >> x;
        if (x < 1 || x > n || f.count(x) == 1) 
        {
            break;
        }
        f.insert(x);
    }
    
    if (f.size() == n) cout << "YES"; else cout << "NO";
    
    return 0;
}

