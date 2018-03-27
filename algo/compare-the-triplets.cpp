// https://www.hackerrank.com/challenges/compare-the-triplets/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int alice[3], bob[3];
    int a = 0, b = 0;
    for (int i = 0; i < 3; ++i) cin >> alice[i];
    for (int i = 0; i < 3; ++i) cin >> bob[i];
    for (int i = 0; i < 3; ++i) {
        if (alice[i] > bob[i]) a++;
        if (alice[i] < bob[i]) b++;
    }
    cout << a << " " << b << endl;
    return 0;
}