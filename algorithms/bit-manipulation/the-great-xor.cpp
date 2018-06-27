// Algorithms > Bit Manipulation > The Great XOR
// Count the number of non-negative integer a's that are less than some x where the bitwise XOR of a and x is greater than x.
//
// https://www.hackerrank.com/challenges/the-great-xor/problem
// https://www.hackerrank.com/contests/w28/challenges/the-great-xor
// challenge id: 27667
//

#include <bits/stdc++.h>

using namespace std;

// Complete the theGreatXor function below.
long theGreatXor(long x) {

    long r = 0;
    long mask = 1;
    while (mask < x)
    {
        if ((mask & x) == 0)
            r += mask;
        mask <<= 1;
    }

    return r;
}

int main()
{
    int q;
    cin >> q;

    while (q--)
    {
        long x;
        cin >> x;

        cout << theGreatXor(x) << endl;
    }

    return 0;
}
