// Security > Functions > Security Functions
//  Complete a function that takes input x and return the remainder of x divided by 11.
// 
// https://www.hackerrank.com/challenges/security-tutorial-functions/problem
// 


#include <bits/stdc++.h>

using namespace std;

int calculate(int x) {
    // Complete this function
    return x % 11;
}

int main() {
    int x;
    cin >> x;
    int result = calculate(x);
    cout << result << endl;
    return 0;
}

