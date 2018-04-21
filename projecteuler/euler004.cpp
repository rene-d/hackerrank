// ProjectEuler+ > Project Euler #4: Largest palindrome product
// Largest palindrome of product of three digit numbers less than N.
//
// https://www.hackerrank.com/contests/projecteuler/challenges/euler004
//

#include <cmath>
#include <cstdio>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    set<int> palindromes;

    for (int a = 100; a < 1000; ++a)
    {
        for (int b = a; b < 1000; ++b)
        {
            int p = a * b;

            // calcule l'«inverse» de p
            int q = 0;
            for (int i = p; i != 0; i /= 10)
                q = 10 * q + i % 10;

            if (p == q)
            {
                // c'est un palindrome
                palindromes.insert(p);
            }
        }
    }

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int p = *(--palindromes.lower_bound(n));
        cout << p << endl;
    }

    return 0;
}
