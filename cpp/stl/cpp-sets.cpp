// Sets-STL
// Learn about the set container. Given a problem with 3 queries, try to answer the queries using the set container.
// 
// https://www.hackerrank.com/challenges/cpp-sets/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    set<int> s;
    int q, op, i;
    
    cin >> q;
    while (q-- != 0)
    {
        cin >> op >> i;
        switch (op) {
            case 1: s.insert(i); break;
            case 2: s.erase(i); break;
            case 3: cout << (s.count(i) != 0 ? "Yes" : "No") << endl;    
        }
    }
    return 0;
}
