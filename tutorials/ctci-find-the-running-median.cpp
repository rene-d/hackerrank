// Heaps: Find the Running Median
// Find the median of the elements after inputting each element.
//
// https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;


template<typename T>
typename std::vector<T>::iterator insert_sorted(std::vector<T> & vec, T const& item)
{
    return vec.insert(std::upper_bound(vec.begin(), vec.end(), item), item);
}

int main()
{
    int n, x;
    vector<int> a;

    cin >> n;
    while (n--)
    {
        cin >> x;

        insert_sorted(a, x);

        // taille 3 : a[1] et a[1] =>  (3-1)/2=1   3/2=1
        // taille 4 : a[1] et a[2] =>  (4-1)/2=1   4/2=2
        double m = (a[(a.size() - 1) / 2] + a[a.size() / 2]) / 2.;

        cout << fixed << setprecision(1) << m << endl;
    }
    return 0;
}
