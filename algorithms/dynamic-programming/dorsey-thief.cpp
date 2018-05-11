// Algorithms > Dynamic Programming > Dorsey Thief
// standard knapsack problem
//
// https://www.hackerrank.com/challenges/dorsey-thief/problem
// https://www.hackerrank.com/contests/101nov13/challenges/dorsey-thief
//

#include <bits/stdc++.h>
using namespace std;


unsigned long knapSack(unsigned long W, const vector<unsigned long>& wt, const vector<unsigned long>& val, size_t n)
{
    vector<unsigned long> dp(W + 1);

    for (size_t i = 0; i < n; ++i)
    {
        for (unsigned long j = W; j >= wt[i]; --j)
        {
            if (dp[j - wt[i]] != 0 || j == wt[i])
                dp[j] = max(dp[j], dp[j - wt[i]] + val[i]);
        }
    }

    return dp[W];
}


int main()
{
    std::ios::sync_with_stdio(false);

    size_t n;
    unsigned long W;
    vector<unsigned long> wt, val;

    cin >> n >> W;

    wt.resize(n);
    val.resize(n);
    for (size_t i = 0; i < n; ++i)
        cin >> val[i] >> wt[i];

    unsigned long r = knapSack(W, wt, val, n);
    if (r == 0)
        cout << "Got caught!" << endl;
    else
        cout << r << endl;

    return 0;
}
