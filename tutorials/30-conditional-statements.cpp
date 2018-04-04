// Day 3: Intro to Conditional Statements
// Get started with conditional statements.
//
// https://www.hackerrank.com/challenges/30-conditional-statements/problem
//

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    if (n % 2 == 1 or (n >= 6 and n <= 20))
        cout << "Weird" << endl;
    else
        cout << "Not Weird" << endl;

    return 0;
}
