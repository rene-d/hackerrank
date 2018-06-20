// Algorithms > Warmup > Solve Me First
// This is an easy challenge to help you start coding in your favorite languages!
//
// https://www.hackerrank.com/challenges/solve-me-first/problem
// challenge id: 2532
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int solveMeFirst(int a, int b) {
    // Hint: Type return a+b; below
    return a + b;
}

int main() {
    int num1, num2;
    int sum;
    cin>>num1>>num2;
    sum = solveMeFirst(num1,num2);
    cout<<sum;
    return 0;
}
