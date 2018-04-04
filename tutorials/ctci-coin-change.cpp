// DP: Coin Change
// Given $m$ distinct dollar coins in infinite quantities, how many ways can you make change for $n$ dollars?
//
// https://www.hackerrank.com/challenges/ctci-coin-change/problem
//

#include <bits/stdc++.h>

using namespace std;

map<pair<size_t,int>, long long> cache;

long long make_change(const vector<int>& coins, size_t coin, int money)
{
    long long nb = 0;

    auto key = make_pair(coin, money);

    auto x = cache.find(key);
    if (x != cache.end())
        return x->second;

    for (size_t i = coin; i < coins.size(); ++i)
    {
        if (money == coins[i])
            nb++;
        else if (money > coins[i])
            nb += make_change(coins, i, money - coins[i]);
    }

    cache[key] = nb;

    return nb;
}

int main(){
    int n;
    int m;
    cin >> n >> m;
    vector<int> coins(m);
    for(int coins_i = 0;coins_i < m;coins_i++){
       cin >> coins[coins_i];
    }
    cout << make_change(coins, 0, n) << endl;
    return 0;
}
