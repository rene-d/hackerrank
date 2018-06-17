// Mathematics > Number Theory > Breaking Sticks
// Find the length of the longest sequence of moves.
//
// https://www.hackerrank.com/challenges/breaking-sticks/problem
// https://www.hackerrank.com/contests/world-codesprint-12/challenges/breaking-sticks
// challenge id: 30186
//

#include <bits/stdc++.h>

using namespace std;


long single_bar(long n)
{
    long moves = 1;

    // décomposition en facteurs premiers
    // et calcul du nombre de "mouvements" au fur et à mesure

    long i = 2;
    while (i * i <= n)
    {
        while (n % i == 0)
        {
            n /= i;
            moves = moves * i + 1;
        }
        i += (i >= 3) ? 2 : 1;
    }

    if (n > 1)
        moves = moves * n + 1;

    return moves;
}


long longestSequence(const vector<long>& a)
{
    long moves = 0;
    for (auto n : a)
    {
        moves += single_bar(n);
    }
    return moves;
}


int main()
{
    vector<long> a;
    int n;

    cin >> n;

    while (n--)
    {
        long x;
        cin >> x;
        a.push_back(x);
    }

    cout << longestSequence(a) << endl;

    return 0;
}
