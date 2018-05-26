// Mathematics > Combinatorics > nCr table
// Help Jim calculating nCr values
//
// https://www.hackerrank.com/challenges/ncr-table/problem
// challenge id: 1232
//

#include <bits/stdc++.h>
using namespace std;

constexpr unsigned MOD = 1000000000;
constexpr unsigned MAX = 1001;

unsigned C[MAX][MAX];


int main()
{
    // Caculate value of Binomial Coefficient in bottom up manner
    //https://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/
    memset(C, 0, sizeof(C));
    for (unsigned i = 0; i < MAX; i++)
    {
        for (unsigned j = 0; j <= i; j++)
        {
            // Base Cases
            if (j == 0 || j == i)
                C[i][j] = 1;

            // Calculate value using previosly stored values
            else
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD;
        }
    }

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        for (unsigned i = 0; i <= n; ++i)
            cout << C[n][i] << " ";
        cout << endl;
    }

    return 0;
}
