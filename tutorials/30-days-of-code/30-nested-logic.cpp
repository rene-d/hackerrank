// Tutorials > 30 Days of Code > Day 26: Nested Logic
// Test your understanding of layered logic by calculating a library fine!
//
// https://www.hackerrank.com/challenges/30-nested-logic/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int d1, m1, y1, d2, m2, y2;
    cin >> d1 >> m1 >> y1;
    cin >> d2 >> m2 >> y2;

    int fine = 0;
    if (y1 > y2)
        fine = 10000;                   // plus d'un an de retard
    else if (y1 == y2)
        if (m1 > m2)
            fine = (m1 - m2) * 500;     // plus d'un mois de retard
        else if (m1 == m2 && d1 > d2)
            fine = (d1 - d2) * 15;      // retard dans le même mois

    cout << fine << endl;

    return 0;
}
