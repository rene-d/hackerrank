// ProjectEuler+ > Project Euler #2: Even Fibonacci numbers
// Even Fibonacci numbers
//
// https://www.hackerrank.com/contests/projecteuler/challenges/euler002
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int t;

    cin >> t;
    while (t--)
    {
        unsigned long n;
        cin >> n;


        unsigned long sum = 0;
        unsigned long a = 1;
        unsigned long b = 2;

        while (b <= n)
        {
            if (b % 2 == 0)
            {
                sum += b;
            }

            unsigned long c = a + b;
            a = b;
            b = c;
        }

        cout << sum << endl;
    }

    return 0;
}
