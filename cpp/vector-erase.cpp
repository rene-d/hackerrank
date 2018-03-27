// Vector-Erase
// Erasing an element from a vector.
// 
// https://www.hackerrank.com/challenges/vector-erase/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    vector<int> v;
    int n, x, a, b;
    
    cin >> n;
    while (n--) { int i; cin >> i; v.push_back(i); }

    cin >> x;
    v.erase(v.begin() + x - 1);
    
    cin >> a >> b;
    v.erase(v.begin() + a - 1, v.begin() + b - 1);
    
    cout << v.size() << endl;
    for (const auto& i : v) cout << i << " ";
    cout << endl;
    
    return 0;
}

