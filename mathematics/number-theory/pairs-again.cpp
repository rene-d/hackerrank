// Mathematics > Number Theory > Satisfactory Pairs
// How many pairs of integers give a solution?
//
// https://www.hackerrank.com/challenges/pairs-again/problem
// https://www.hackerrank.com/contests/w26/challenges/pairs-again
// challenge id: 27017
//

#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<vector<unsigned>> divs;
    vector<bool> used;
    unsigned n;

    cin >> n;

    divs.resize(n + 1);
    used.resize(n + 1);

    // calcule les diviseurs de i ∈ [1, n]
    for (unsigned i = 1; i <= n; i++)
    {
        for (unsigned j = i; j <= n; j += i)
        {
            divs[j].push_back(i);
        }
    }

    unsigned nb = 0;

    for (unsigned a = 1; a <= n; a++)
    {
        for (unsigned x = 1; a * x <= n; x++)
        {
            for (unsigned d : divs[n - a * x])
            {
                if (a < d)
                {
                    if (!used[d])
                    {
                        used[d] = true;
                        nb++;
                    }
                }
            }
        }

        for (unsigned x = 1; a * x <= n; x++)
        {
            for (unsigned d : divs[n - a * x])
            {
                used[d] = false;
            }
        }
    }


    cout << nb << endl;

    return 0;
}
