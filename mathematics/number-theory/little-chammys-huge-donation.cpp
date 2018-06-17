// Mathematics > Number Theory > Little Ashish's Huge Donation
// Help Ashish calculate donations.
//
// https://www.hackerrank.com/challenges/little-chammys-huge-donation/problem
// https://www.hackerrank.com/contests/infinitum-sep14/challenges/little-chammys-huge-donation
// challenge id: 3334
//

#include <bits/stdc++.h>
using namespace std;

// note: sum i^2 from i=1 to n = 1/6 n (1 + n) (1 + 2 n)

int main()
{
    int t;
    unsigned long i, x;
    vector<unsigned long>   values;

    values.resize(310723);      // 310723 = solution de sum(i^2) = 10^16
    for (i = 1; ; ++i)
    {
        x = i * (i + 1) * (2 * i + 1) / 6;
        if (x > 10000000000000000) break;
        values[i] = x;
    }

    cin >> t;
    while (t--)
    {
        cin >> x;

        auto i = upper_bound(values.cbegin(), values.cend(), x);
        --i;

        cout << (i - values.cbegin()) << endl;
    }
    return 0;
}
