// Hash Tables: Ransom Note
// Given two sets of dictionaries, tell if one of them is a subset of the other.
//
// https://www.hackerrank.com/challenges/ctci-ransom-note/problem
//
#include <bits/stdc++.h>

using namespace std;


int main()
{
    size_t m;
    size_t n;
    cin >> m >> n;

    map<string, int> magazine;
    while (m-- != 0)
    {
        string word;
        cin >> word;
        magazine[word]++;
    }

    while (n-- != 0)
    {
        string word;
        cin >> word;

        auto i = magazine.find(word);

        // mot non trouvé ou épuisé
        if (i == magazine.end() || i->second == 0)
        {
            cout << "No\n";
            return 0;
        }
        i->second--;
    }

    cout << "Yes\n";
    return 0;
}
