// Find the Point
//
// https://www.hackerrank.com/challenges/find-point/problem

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    for (auto i = 0; i < n; ++i)
    {
        int px, py, qx, qy;
        cin >> px >> py >> qx >> qy;
        cout << (qx + qx - px) << " " << (qy + qy - py) << endl;
    }
    return 0;
}
