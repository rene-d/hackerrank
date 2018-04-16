// Tutorials > 30 Days of Code > Day 16: Exceptions - String to Integer
// Can you determine if a string can be converted to an integer?
//
// https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
//

#include <bits/stdc++.h>

using namespace std;


int main()
{
    try
    {
        string s;

        cin >> s;
        cout << stoi(s) << endl;
    }
    catch (invalid_argument& e)
    {
        cout << "Bad String" << endl;
    }
    return 0;
}
