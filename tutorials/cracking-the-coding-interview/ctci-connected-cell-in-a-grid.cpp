// DFS: Connected Cell in a Grid
// Find the largest connected region in a 2D Matrix.
// 
// https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
// 

#include <bits/stdc++.h>

using namespace std;


struct coord
{
    int x;
    int y;  
};

int get_biggest_region(int n, int m, vector<vector<int>>& grid) 
{
    int size_max = 0;
 
    for (int x = 0; x < n; ++x) 
    {    
        for (int y = 0; y < m; ++y) 
        {            
            if (grid[x][y] == 1)
            {
                stack<coord>    fill;
                fill.push(coord{x, y});
                int size = 0;
                
                while (! fill.empty())
                {
                    coord p = fill.top();                    
                    fill.pop();
                    
                    if (grid[p.x][p.y] != 1) continue;
                    
                    grid[p.x][p.y] = 2;
                    size++;
                    
                    if (p.x > 0   && p.y > 0   && grid[p.x - 1][p.y - 1] == 1) fill.push(coord{p.x - 1, p.y - 1});
                    if (p.x > 0                && grid[p.x - 1][p.y    ] == 1) fill.push(coord{p.x - 1, p.y    });
                    if (p.x > 0   && p.y < m-1 && grid[p.x - 1][p.y + 1] == 1) fill.push(coord{p.x - 1, p.y + 1});
                    if (p.x < n-1 && p.y > 0   && grid[p.x + 1][p.y - 1] == 1) fill.push(coord{p.x + 1, p.y - 1});
                    if (p.x < n-1              && grid[p.x + 1][p.y    ] == 1) fill.push(coord{p.x + 1, p.y    });
                    if (p.x < n-1 && p.y < m-1 && grid[p.x + 1][p.y + 1] == 1) fill.push(coord{p.x + 1, p.y + 1});

                    if (             p.y > 0   && grid[p.x    ][p.y - 1] == 1) fill.push(coord{p.x    , p.y - 1});
                    if (             p.y < m-1 && grid[p.x    ][p.y + 1] == 1) fill.push(coord{p.x    , p.y + 1});
                }
                
                if (size > size_max)
                    size_max = size;
            }
        }
    }
    
    return size_max;
}

int main(){
    int n;
    cin >> n;
    int m;
    cin >> m;
    vector<vector<int>> grid(n,vector<int>(m));
    for(int grid_i = 0;grid_i < n;grid_i++){
       for(int grid_j = 0;grid_j < m;grid_j++){
          cin >> grid[grid_i][grid_j];
       }
    }
    cout << get_biggest_region(n, m, grid) << endl;
    return 0;
}
