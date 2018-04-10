// Lower Bound-STL
// Given N numbers, you have to find the smallest integer greater than the given number and print the index of that number.
// 
// https://www.hackerrank.com/challenges/cpp-lower-bound/problem
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
    int n, q;
    
    cin >> n;
    while (n--) { int i; cin >> i; v.push_back(i); }
    
    cin >> n;
    while (n-- != 0)
    {
        cin >> q;
        
        vector<int>::const_iterator r = lower_bound(v.begin(), v.end(), q);
        
        cout << ((*r == q) ? "Yes " : "No ")
             << 1 + (r - v.begin()) << endl;
    }

    return 0;
}

