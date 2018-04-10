// Day 2: Operators
// Start using arithmetic operators.
//
// https://www.hackerrank.com/challenges/30-operators/problem
//

#include <bits/stdc++.h>

using namespace std;

int main() {
    double meal_cost;
    cin >> meal_cost;
    int tip_percent;
    cin >> tip_percent;
    int tax_percent;
    cin >> tax_percent;

    cout << "The total meal cost is "
         << round(meal_cost * (1 + tip_percent / 100. + tax_percent / 100.))
         << " dollars." << endl;

    return 0;
}
