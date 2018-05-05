// ProjectEuler+ > Project Euler #3: Largest prime factor
// Figuring out prime numbers, factors, and then both of them together!
//
// https://www.hackerrank.com/contests/projecteuler/challenges/euler003
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


unsigned long largest_prime_factor(unsigned long n)
{
    unsigned long i = 2;
    unsigned long largest = 2;

    while (i * i <= n)
    {
        while (n % i == 0)
        {
            n = n / i;
            largest = i;
        }

        i += (i >= 3) ? 2 : 1;
    }

    return (n > 1) ? n : largest;
}


int main()
{
    int t;

    cin >> t;
    while (t--)
    {
        unsigned long n;
        cin >> n;
        cout << largest_prime_factor(n) << endl;

    }
    return 0;
}
