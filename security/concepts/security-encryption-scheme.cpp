// Security > Terminology and Concepts > Security Encryption Scheme
// Count the number of bijections and the number of keys that produce different encryption functions.
// 
// https://www.hackerrank.com/challenges/security-encryption-scheme/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// la réponse est: n!

int main() {
    int n;
    int f = 1;
    cin >> n;
    for (int i = 1; i <= n; ++i) f *= i;
    cout << f;
    return 0;
}

