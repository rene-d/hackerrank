// https://www.hackerrank.com/challenges/simple-array-sum/problem

//#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int simpleArraySum(size_t, vector <int> ar) {
    // Complete this function
    int sum = 0;
    for (auto i : ar) sum += i;
    return sum;
}

int main() {
    size_t n;
    cin >> n;
    vector<int> ar(n);
    for(size_t ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = simpleArraySum(n, ar);
    cout << result << endl;
    return 0;
}

