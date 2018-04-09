// Day 7: Arrays
// Getting started with Arrays.
//
// https://www.hackerrank.com/challenges/30-arrays/problem
//

#include <bits/stdc++.h>

using namespace std;


int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++)
    {
       cin >> arr[arr_i];
    }

    for(int arr_i = n;arr_i > 0;)
    {
       cout << arr[--arr_i] << " ";
    }
    cout << endl;

    return 0;
}
