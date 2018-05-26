// Mathematics > Number Theory > Largest Non-Coprime Submatrix
// Given a matrix find the largest coprime submatrix.
//
// https://www.hackerrank.com/challenges/largest-coprime-submatrix/problem
// challenge id: 781
//

#include <bits/stdc++.h>
using namespace std;


// solution: brute force...

int gcd(int u, int v)
{
    while (v != 0)
    {
        int r = u % v;
        u = v;
        v = r;
    }
    return u;
}


int main()
{
    int matrix[200][200];
    size_t n, m;
    cin >> n >> m;

    for (size_t i = 0; i < n; ++i)
    {
        for (size_t j = 0; j < m; ++j)
        {
            cin >> matrix[i][j];
        }
    }

    size_t r = 0;

    for (size_t x1 = 0; x1 < n; ++x1)
    {
        for (size_t y1 = 0; y1 < m; ++y1)
        {
            if (r > (n - x1) * (m - y1)) break;

            // gcd entre (x1,y1) et (x2,y2)
            int sub_gcd[200] = {0};

            for (size_t x2 = x1; x2 < n; ++x2)
            {
                int g = 0;
                for (size_t y2 = y1; y2 < m; ++y2)
                {
                    g = gcd(gcd(g, matrix[x2][y2]), sub_gcd[y2]);
                    sub_gcd[y2] = g;

                    if (g == 1) break;

                    r = max(r, (x2 - x1 + 1) * (y2 - y1 + 1));
                }
            }
        }
    }

    cout << r << endl;

    return 0;
}
