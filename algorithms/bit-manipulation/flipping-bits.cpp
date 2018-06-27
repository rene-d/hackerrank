// Algorithms > Bit Manipulation > Flipping bits
// Flip bits in its binary representation.
//
// https://www.hackerrank.com/challenges/flipping-bits/problem
// https://www.hackerrank.com/contests/101hack20/challenges/flipping-bits
// challenge id: 5529
//

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        uint32_t a;
        cin >> a;
        cout << ~a << endl;
    }

    return 0;
}
