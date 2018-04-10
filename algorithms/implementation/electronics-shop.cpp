// Electronics Shop
// Determine the most expensive Keyboard and USB drive combination Monica can purchase within her budget.
// 
// https://www.hackerrank.com/challenges/electronics-shop/problem
// 

#include <bits/stdc++.h>

using namespace std;

int getMoneySpent(const vector<int>& keyboards, const vector<int>& drives, int s)
{
    // Complete this function
    int smax = -1;
    for (const auto& k : keyboards)
    {
        for (const auto& d : drives)
        {
            if (k + d <= s && k + d > smax)
            {
                smax = k + d;
            }
            
        }
    }
    return smax;
}

int main() {
    int s;
    int n;
    int m;
    cin >> s >> n >> m;
    vector<int> keyboards(n);
    for(int keyboards_i = 0; keyboards_i < n; keyboards_i++){
       cin >> keyboards[keyboards_i];
    }
    vector<int> drives(m);
    for(int drives_i = 0; drives_i < m; drives_i++){
       cin >> drives[drives_i];
    }
    //  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    int moneySpent = getMoneySpent(keyboards, drives, s);
    cout << moneySpent << endl;
    return 0;
}
