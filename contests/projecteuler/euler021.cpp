// ProjectEuler+ > Project Euler #21: Amicable numbers
// Proper and improper divisions.
//
// https://www.hackerrank.com/contests/projecteuler/challenges/euler021
// challenge id: 2647
//

#include <bits/stdc++.h>

using namespace std;

const unsigned MAX = 100000;


unsigned sum_of_divisors(unsigned n)
{
    unsigned temp = n;
    unsigned sum = 1;
    for (unsigned i = 2; i < n; ++i)
    {
        n = temp / i;
        if (temp % i == 0)
        {
            sum += i + n;
            if (sum > MAX)
                return 0;
        }
    }
    return sum;
}


int main()
{
    vector<unsigned> sod(MAX + 1, 0u);
    vector<unsigned> ami(MAX + 1, 0u);

    for (unsigned i = 1; i <= MAX; ++i)
        sod[i] = sum_of_divisors(i);

    unsigned x = 0;
    for (unsigned i = 1; i <= MAX; ++i)
    {
        unsigned a = sod[i];
        if (a != i && a != 0)
        {
            if (i == sod[a])
                x += i;
        }
        ami[i] = x;
    }

    int t;
    unsigned n;
    cin >> t;
    while (t--)
    {
        cin >> n;
        cout << ami[n - 1] << endl;
    }
}
