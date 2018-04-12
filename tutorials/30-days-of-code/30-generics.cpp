// Tutorials > 30 Days of Code > Day 21: Generics
// Welcome to Day 21! Review generics in this challenge!
//
// https://www.hackerrank.com/challenges/30-generics/problem
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;
// (skeliton_head) ----------------------------------------------------------------------

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

template<typename T>
void printArray(const vector<T>& a)
{
    for (auto i : a)
        cout << i << endl;
}

// (skeliton_tail) ----------------------------------------------------------------------
int main() {
	int n;

	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}

	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
