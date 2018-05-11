// Security > Functions > Security Functions II
// Complete the function that takes x as the input and returns (x*x)
//
// https://www.hackerrank.com/challenges/security-function-ii/problem
//

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
// (skeliton_head) ----------------------------------------------------------------------

/*
 * Complete the function below.
 */
int the_function(int x) {

    return x * x;
}

// (skeliton_tail) ----------------------------------------------------------------------
int main() {
    int res;
    int _x;
    cin >> _x;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');

    res = the_function(_x);
    cout << res << endl;

    return 0;
}
