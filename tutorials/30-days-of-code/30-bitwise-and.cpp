// Tutorials > 30 Days of Code > Day 29: Bitwise AND
// Apply everything we've learned in this bitwise AND challenge.
//
// https://www.hackerrank.com/challenges/30-bitwise-and/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;

        int max = 0;
        for (int i = 2; i < n; ++i)
        {
            for (int j = i + 1; j <= n; ++j)
            {
                int ij = i & j;
                if (ij < k && ij > max) max = ij;
            }
        }

        cout << max << endl;
    }
    return 0;
}
