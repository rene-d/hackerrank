// Algorithms > Implementation > Ema's Supercomputer
// Determine the product of the areas of two pluses on a grid.
//
// https://www.hackerrank.com/challenges/two-pluses/problem
//

#include <bits/stdc++.h>

using namespace std;

#pragma GCC diagnostic ignored "-Wsign-conversion"
#pragma GCC diagnostic ignored "-Wsign-compare"
#pragma GCC diagnostic ignored "-Wshorten-64-to-32"


template<typename T>
typename std::vector<T>::iterator insert_sorted(std::vector<T> & vec, T const& item)
{
    return vec.insert(std::upper_bound(vec.begin(), vec.end(), item,
                                       [] (const T&a, const T& b)-> bool
                                       {
                                           return std::get<0>(a) > std::get<0>(b);
                                       }), item);
}

int twoPluses(const vector<string>& grid)
{
    // Complete this function
    vector<tuple<int, int, int>> plus;

    int n = grid.size();
    int m = grid[0].length();

    for (int x = 0; x < n; ++x)
    {
        for (int y = 0; y < m; ++y)
        {
            int k = 0;
            while (x + k < n && y + k < m && x - k >= 0 && y - k >= 0
                    && grid[x][y + k] == 'G'
                    && grid[x][y - k] == 'G'
                    && grid[x - k][y] == 'G'
                    && grid[x + k][y] == 'G')
            {
                //int s = k * 4 + 1;
                tuple<int, int, int> v(k, x, y);
                insert_sorted(plus, v);
                ++k;
            }
        }
    }

    vector<string> check = grid;
    char    flag = '+';
    int     max = 0;

    for (int i = 0; i < plus.size() - 1; ++i)
    {
        int k1, x, y;

        std::tie(k1, x, y) = plus[i];

        // impossible de trouver un produit supérieur
        if ((k1 * 4 + 1) * (k1 * 4 + 1) <= max)
            break;

        for (int k = k1; k >= 0; k--)
        {
            check[x][y - k] = flag;
            check[x][y + k] = flag;
            check[x - k][y] = flag;
            check[x + k][y] = flag;
        }

        for (int j = i + 1; j < plus.size(); ++j)
        {
            bool overlap = false;
            int k2, x, y;

            std::tie(k2, x, y) = plus[j];

            for (int k = k2; k >= 0; k--)
            {
                if (   check[x][y - k] == flag
                    || check[x][y + k] == flag
                    || check[x - k][y] == flag
                    || check[x + k][y] == flag)
                {
                    overlap = true;
                    break;
                }
            }

            if (overlap == false)
            {
                int kk = (k1 * 4 + 1) * (k2 * 4 + 1);
                if (kk > max)
                {
                    max = kk;
                    break;      // les produits suivants seront plus petits
                }
            }
        }

        // rétablit la grille
        for (int k = k1; k >= 0; k--)
        {
            check[x][y - k] = 'G';
            check[x][y + k] = 'G';
            check[x - k][y] = 'G';
            check[x + k][y] = 'G';
        }

    }

    return max;
}

int main()
{
    int n;
    int m;
    cin >> n >> m;
    vector<string> grid(n);
    for(int grid_i = 0; grid_i < n; grid_i++){
       cin >> grid[grid_i];
    }
    int result = twoPluses(grid);
    cout << result << endl;
    return 0;
}
