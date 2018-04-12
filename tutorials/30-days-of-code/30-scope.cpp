// Tutorials > 30 Days of Code > Day 14: Scope
// Learn about the scope of an identifier.
//
// https://www.hackerrank.com/challenges/30-scope/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;

  	public:
  	int maximumDifference;
// (skeliton_head) ----------------------------------------------------------------------

    Difference(const vector<int>& a)
    {
        maximumDifference = *std::max_element(a.begin(), a.end()) - *std::min_element(a.begin(), a.end());
    }

    void computeDifference() const
    {}

// (skeliton_tail) ----------------------------------------------------------------------
}; // End of Difference class

int main() {
    int N;
    cin >> N;

    vector<int> a;

    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;

        a.push_back(e);
    }

    Difference d(a);

    d.computeDifference();

    cout << d.maximumDifference;

    return 0;
}
