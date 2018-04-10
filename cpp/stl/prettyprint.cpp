// Print Pretty
// This challenge will test your knowledge of the STL <iomanip> library.
// 
// https://www.hackerrank.com/challenges/prettyprint/problem
// 

#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;
// (skeliton_head) ----------------------------------------------------------------------

        // LINE 1 
        cout << hex << left << showbase << nouppercase;
        cout << (long long unsigned int)A << endl;

        // LINE 2
        cout << dec << right << setw(15) << setfill('_') << showpos << fixed << setprecision(2);
        cout << B << endl;

        // LINE 3
        cout << scientific << uppercase << noshowpos << setprecision(9);
        cout << C << endl;

// (skeliton_tail) ----------------------------------------------------------------------
	}
	return 0;

}