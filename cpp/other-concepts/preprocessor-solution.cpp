// Preprocessor Solution
// Create preprocessor macros to make the existing code work.
//
// https://www.hackerrank.com/challenges/preprocessor-solution/problem
//

#define INF 1000000000

#define FUNCTION(f, comp) \
        void f(int& a, int b) \
        { if (b comp a) a = b; }

#define io(v) \
    cin >> v

#define toStr(x) #x

#define foreach(v, i) \
    for (size_t i = 0; i < v.size(); ++i)


// (skeliton_tail) ----------------------------------------------------------------------
#include <iostream>
#include <vector>
using namespace std;

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
	return 0;

}
