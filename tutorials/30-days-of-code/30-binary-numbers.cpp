// Tutorials > 30 Days of Code > Day 10: Binary Numbers
// Find the maximum number of consecutive 1's in the base-2 representation of a base-10 number.
//
// https://www.hackerrank.com/challenges/30-binary-numbers/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int n;
    int one = 0;
    int answer = 0;
    cin >> n;
    while (n != 0)
    {
        if ((n & 1) == 1)
        {
            one++;
            answer = max(answer, one);
        }
        else
            one = 0;

        n >>= 1;
    }
    cout << answer << endl;
    return 0;
}
