// Security > Terminology and Concepts > Security - Message Space and Ciphertext Space
// Given a message, you need to find what message you obtain if you shift each digit in the message string ( 1 to the right and cyclic).
// 
// https://www.hackerrank.com/challenges/security-message-space-and-ciphertext-space/problem
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
    cin >> s;
    for (auto&& i : s)
    {
        cout << (i - '0' + 1) % 10;
    }
    return 0;
}

