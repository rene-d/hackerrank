// Mathematics > Number Theory > Divisor Exploration 3
// Find the value given at the root of a tree constructing by the given rules.
//
// https://www.hackerrank.com/challenges/divisor-exploration-3/problem
// https://www.hackerrank.com/contests/infinitum18/challenges/divisor-exploration-3
// challenge id: 12630
//

// C++ version, I can't find a way to optimize these instructions
//        num = (p * num * c_den  - c_num * den) % MOD
//        den = (den * (p - 1) * c_den) % MOD
// in Python (it's ok with numba.jit...)


#include <bits/stdc++.h>
using namespace std;

#define MOD  1000000007

vector<int64_t>    primes;


void init_primes()
{
    int64_t PRIME_1000 = 7919;
    vector<bool> sieve(1 + PRIME_1000, true);
    primes.reserve(1000);
    for (int64_t n = 2; n <= PRIME_1000; ++n)
    {
        if (sieve[n])
        {
            primes.push_back(n);
            for (int64_t i = n; i <= PRIME_1000; i += n)
                sieve[i] = false;
        }
    }
}


int64_t modinv(int64_t a, int64_t b)
{
    int64_t t, nt, r, nr, q, tmp;
    if (b < 0) b = -b;
    if (a < 0) a = b - (-a % b);
    t = 0;  nt = 1;  r = b;  nr = a % b;
    while (nr != 0) {
        q = r/nr;
        tmp = nt;  nt = t - q*nt;  t = tmp;
        tmp = nr;  nr = r - q*nr;  r = tmp;
    }
    if (r > 1) return -1;  /* No inverse */
    if (t < 0) t += b;
    return t;
}


int64_t fast_f(int64_t i, int64_t p, int64_t a)
{
    int64_t num, den;
    int64_t c_num, c_den;

    num = 1; den = 1;
    for (int64_t i = 0; i < a; ++i)
        num = (num * p) % MOD;

    c_num = 1; c_den = 1;

    for (int64_t j = 2; j <= i; ++j)
    {
        if (j > 2)
        {
            c_num = (c_num * (a + j - 2)) % MOD;
            c_den = (c_den * (j - 2)) % MOD;
        }

        num = (p * ((num * c_den) % MOD) % MOD - c_num * den) % MOD; if (num < 0) num += MOD;
        den = (((den * (p - 1)) % MOD) * c_den) % MOD;
    }

    num = (num * modinv(den, MOD)) % MOD;

    return num;
}


int64_t solve(int64_t m, int64_t a, int64_t d)
{
    int64_t res = 1;
    for (int64_t i = 0; i < m; ++i)
        res = (res * fast_f(d, primes[i], a + i + 1)) % MOD;

    return res;
}


int main()
{
    int64_t m, a, d;
    int t;

    init_primes();

    cin >> t;
    while (t--)
    {
        cin >> m >> a >> d;
        cout << solve(m, a, d) << endl;
    }

    return 0;
}
