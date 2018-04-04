// Day 1: Data Types
// Get started with data types.
//
// https://www.hackerrank.com/challenges/30-data-types/problem
//

#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
// (skeliton_head) ----------------------------------------------------------------------

    // Declare second integer, double, and String variables.
    int i2;
    double d2;
    string s2;

    // Read and save an integer, double, and String to your variables.
    cin >> i2 >> d2; getline(cin, s2);
    getline(cin, s2);

    // Print the sum of both integer variables on a new line.
    cout << i + i2 << endl;

    // Print the sum of the double variables on a new line.
    cout << fixed << setprecision(1) << d + d2 << endl;

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s << s2 << endl;

// (skeliton_tail) ----------------------------------------------------------------------
    return 0;
}
