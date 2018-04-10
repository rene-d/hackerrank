// Cavity Map
// Depict cavities on a square map
//
// https://www.hackerrank.com/challenges/cavity-map/problem
//

#include <bits/stdc++.h>

using namespace std;

vector<string> cavityMap(size_t n, const vector<string>& grid) {
    // Complete this function
    vector<string> result = grid;

    for (size_t i = 1; i < n - 1; ++i)
    {
        for (size_t j = 1; j < n - 1; ++j)
        {
            char v = grid[i][j];
            if (v > grid[i - 1][j] && v > grid[i + 1][j] && v > grid[i][j - 1] && v > grid[i][j + 1])
            {
                result[i][j] = 'X';
            }
        }
    }

    return result;
}

int main() {
    size_t n;
    cin >> n;

    vector<string> grid(n);
    for (size_t grid_i = 0; grid_i < n; grid_i++) {
       cin >> grid[grid_i];
    }

    vector<string> result = cavityMap(n, grid);
    for (const auto& row : result) {
        cout << row << endl;
    }

    return 0;
}
