// https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(const string& str) {
   // Complete this function
    stringstream ss(str);
    vector<int> v;

    while (! ss.eof())
    {
        int i;
        ss >> i;
        v.push_back(i);

        char c;
        ss >> c;
        if (c != ',') break;
    }
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(size_t i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

