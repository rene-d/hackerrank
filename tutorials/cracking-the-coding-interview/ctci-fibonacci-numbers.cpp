// Recursion: Fibonacci Numbers
// Compute the $n^{th}$ Fibonacci number.
//
// https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
//

#include <iostream>

using namespace std;

int fibonacci(int n) {

    // Complete the function.
    if (n < 2) return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}
