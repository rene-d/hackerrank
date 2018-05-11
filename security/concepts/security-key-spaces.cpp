// Security > Terminology and Concepts > Security Key Spaces
// Consider a message that consists of decimal digits and a key, e, which operates by shifting each digit by e places. Find the corresponding cipher text.
// 
// https://www.hackerrank.com/challenges/security-key-spaces/problem
// 

#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string s;
    int k;
    cin >> s;
    cin >> k;
    for (auto&& i : s)
    {
        cout << (i - '0' + k) % 10;
    }
    return 0;
}

