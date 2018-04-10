// Maximum Perimeter Triangle
// Find the triangle having the maximum perimeter.
//
// https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
//

#include <bits/stdc++.h>

using namespace std;

void maximumPerimeterTriangle(vector<int> l)
{
    if (l.size() >= 3)
    {
        std::sort(l.begin(), l.end(), [](int a, int b) -> bool { return a > b; });

        // sélectionne les 3 plus grands nombres qui forment un triangle non aplati
        // 1 1 3 : pas de triangle
        // 1 2 3 : triangle aplati
        // 1 3 3 : ok
        for (size_t i = 0; i < l.size() - 2; ++i)
        {
            if (l[i] < l[i + 1] + l[i + 2])
            {
                cout << l[i + 2] << " " << l[i + 1] << " " << l[i] << endl;
                return;
            }
        }
    }

    cout << "-1" << endl;
}

int main()
{
    size_t n;
    cin >> n;
    vector<int> l(n);
    for(size_t l_i = 0; l_i < n; l_i++)
    {
       cin >> l[l_i];
    }

    maximumPerimeterTriangle(l);

    return 0;
}
