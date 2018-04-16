// Tutorials > 30 Days of Code > Day 25: Running Time and Complexity
// Determine if a number is prime in optimal time!
//
// https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


bool is_prime(int n)
{
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    int d = 3;
    while (d * d <= n)
    {
        if (n % d == 0) return false;
        d += 2;
    }
    return true;
}

int main()
{
    int q;
    cin >> q;
    while (q--)
    {
        int n;
        cin >> n;
        cout << (is_prime(n) ? "Prime" : "Not prime") << endl;
    }
    return 0;
}
