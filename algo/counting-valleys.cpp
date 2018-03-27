// Counting Valleys
// Count the valleys encountered during vacation.
// 
// https://www.hackerrank.com/challenges/counting-valleys/problem
// 

#include <bits/stdc++.h>


using namespace std;

int countingValleys(const string& s) {
    // Complete this function
    int valleys = 0;
    int alt = 0;
    
    for (auto c : s)
    {
        int new_alt = alt + ((c == 'U') ? +1 : -1);
        
        if (alt == 0 && new_alt == -1) valleys ++;
        
        alt = new_alt;
    }

    return valleys;
}

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int result = countingValleys(s);
    cout << result << endl;
    return 0;
}

