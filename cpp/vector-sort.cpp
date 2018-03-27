// https://www.hackerrank.com/challenges/vector-sort/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, x;
    vector<int>     v;
    
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        cin >> x;
        v.push_back(x);
    }

    std::sort(v.begin(), v.end());
    for (const auto& i :v)
        cout << i << " ";
    cout << endl;

    return 0;
}
