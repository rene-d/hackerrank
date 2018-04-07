// Day 6: Let's Review
// Characters and Strings
//
// https://www.hackerrank.com/challenges/30-review-loop/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        string s;
        cin >> s;

        for (size_t i = 0; i < s.length(); ++i)
            if (i % 2 == 0) cout << s[i];
        cout << ' ';
        for (size_t i = 0; i < s.length(); ++i)
            if (i % 2 == 1) cout << s[i];
        cout << endl;
    }

    return 0;
}
