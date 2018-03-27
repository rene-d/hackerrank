// https://www.hackerrank.com/challenges/arrays-ds/problem

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    size_t n;
    cin >> n;
    vector<int> arr(n);
    for(size_t arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    for (auto i = arr.rbegin(); i != arr.rend(); ++i)
        cout << *i << " ";
    cout << endl;
    return 0;
}
