// Recursion: Davis' Staircase
// Find the number of ways to get from the bottom of a staircase to the top if you can jump 1, 2, or 3 stairs at a time.
//
// https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

// nota: le testcase max est n=36
// et ça tient dans un int 32-bit

map<int, int> cache;

int staircase(int n)
{
    int nb = 0;

    if (n == 0)
        return 1;

    auto i = cache.find(n);
    if (i != cache.end())
    {
        return i->second;
    }

    for (int i = 1; i <= 3; ++i)
    {
        if (n >= i)
            nb += staircase(n - i);
    }

    cache[n] = nb;

    return nb;
}

int main() {
    int q;
    cin >> q;
    while (q--)
    {
        int n;
        cin >> n;
        cout << staircase(n) << endl;
    }

    return 0;
}
