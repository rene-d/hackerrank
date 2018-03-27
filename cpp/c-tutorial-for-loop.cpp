// https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    const char *digits[] = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    int n1, n2;
    cin >> n1 >> n2;
    for (int n = n1; n <= n2; ++n) {
        if (n < 1) {
            // rien
        }
        else if (n <= 9) cout << digits[n] << endl;
        else if (n % 2 == 0)
            cout << "even" << endl;
        else
            cout << "odd" << endl;
    }
    return 0;
}

