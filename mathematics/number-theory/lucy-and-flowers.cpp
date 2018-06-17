// Mathematics > Number Theory > Lucy and Flowers
// Help Lucy's father with a computation involving flowers
//
// https://www.hackerrank.com/challenges/lucy-and-flowers/problem
// https://www.hackerrank.com/contests/w4/challenges/lucy-and-flowers
// challenge id: 2414
//

#include <bits/stdc++.h>

using namespace std;


constexpr unsigned MAX = 5001;
constexpr unsigned MOD = 1000000009;

unsigned catalan[MAX];
unsigned C[MAX][MAX];


unsigned mult(unsigned a, unsigned b, unsigned mod)
{
    unsigned long long la = a;
    unsigned long long lb = b;

    return (unsigned)((la * lb) % mod);
}


void precompute()
{
    // calcule les nombres de Catalan
    // https://oeis.org/A000108
	catalan[0] = 1;
    catalan[1] = 1;
	for (unsigned i = 2; i < MAX; ++i)
	{
        unsigned c = 0;
		for (unsigned j = 1; j <= i; j++)
			c = (c + mult(catalan[j - 1], catalan[i - j], MOD)) % MOD;
        catalan[i] = c;
	}

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
}


// la solution est Σ C(n, i) * catalan(i)
//
unsigned solve(unsigned n)
{
    unsigned r = 0;
    for (unsigned i = 1; i <= n; i++)
        r = (r + mult(C[n][i], catalan[i], MOD)) % MOD;
    return r;
}


int main()
{
    precompute();
    int t;
    cin >> t;
    while (t--)
    {
        unsigned n;
        cin >> n;
        cout << solve(n) << endl;
    }
    return 0;
}
