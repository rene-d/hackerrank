// Bit Manipulation: Lonely Integer
// Find the unique element in an array of integer pairs.
//
// https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
//

#include <bits/stdc++.h>

using namespace std;

int lonely_integer(const vector<int>& a)
{
    int result = 0;

    for (auto i : a)
    {
        result ^= i;
    }

    return result;
}

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
       cin >> a[a_i];
    }
    cout << lonely_integer(a) << endl;
    return 0;
}
