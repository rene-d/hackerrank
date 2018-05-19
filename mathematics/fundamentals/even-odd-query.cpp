// https://www.hackerrank.com/challenges/even-odd-query/problem

#include <iostream>
#include <vector>

using namespace std;

#pragma GCC diagnostic ignored "-Wsign-conversion"

int main()
{
    vector<int> a;
    int n, q, x, y, t;
    cin >> n;

    while (n--)
    {
        cin >> t;
        a.push_back(t);
    }

    cin >> q;
    while (q--)
    {
        cin >> x >> y;

        if (a[x - 1] % 2 == 1 || x > y || (x < y && a[x] == 0))
            cout << "Odd" << endl;
        else
            cout << "Even" << endl;
    }

    return 0;
}