// Exceptional Server
// Handle server errors.
// 
// https://www.hackerrank.com/challenges/exceptional-server/problem
//

// les gars d'hackerrank n'assoient un peu sur la qualité et la sécurité du code
// après, faut pas s'étonner de la qualité du code industrialisé...
#pragma GCC diagnostic ignored "-Wsign-compare"
#pragma GCC diagnostic ignored "-Wsign-conversion"
#pragma GCC diagnostic ignored "-Wshorten-64-to-32"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wfloat-conversion"

// de plus, ce challenge ne fonctionne pas avec clang, il est ni pertinent
// ni judicieux


#include <iostream>
#include <exception>
#include <string>
#include <stdexcept>
#include <vector>
#include <cmath>
using namespace std;

class Server {
private:
	static int load;
public:
	static int compute(long long A, long long B) {
		load += 1;
		if(A < 0) {
			throw std::invalid_argument("A is negative");
		}
		vector<int> v(A, 0);
		int real = -1, cmplx = sqrt(-1);
		if(B == 0) throw 0;
		real = (A/B)*real;
		int ans = v.at(B);
		return real + A - B*ans;
	}
	static int getLoad() {
		return load;
	}
};
int Server::load = 0;

int main() {
	int T; cin >> T;
	while(T--) {
		long long A, B;
		cin >> A >> B;
// (skeliton_head) ----------------------------------------------------------------------

		/* Enter your code here. */
        try {
            cout << Server::compute(A, B) << endl;
        }
        catch (bad_alloc& e)
        {
            cout << "Not enough memory" << endl;
        }
        catch (exception& e)
        {
            cout << "Exception: " << e.what() << endl;
        }
        catch (...)
        {
            cout << "Other Exception" << endl;
        }

// (skeliton_tail) ----------------------------------------------------------------------
	}
	cout << Server::getLoad() << endl;
	return 0;
}