// https://www.hackerrank.com/challenges/bitset-1/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    unsigned int N, S, P, Q;
    unsigned int i, a;

    vector<bool> present;       // nota: vector<bool> est optimisé
    present.resize(0x80000000);

    if (scanf("%u %u %u %u", &N, &S, &P, &Q) != 4)
        exit(2);

    int nb = 0;
    i = 0;
    a = S % 0x80000000;
    do {
        if (! present[a]) {
            ++nb;
            present[a] = true;
        }
        a = (a * P + Q) % 0x80000000;
    } while (++i < N);
    cout << nb << endl;

    return 0;
}