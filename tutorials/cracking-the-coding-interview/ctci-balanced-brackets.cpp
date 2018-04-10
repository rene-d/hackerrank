// Stacks: Balanced Brackets
// Given a string containing three types of brackets, determine if it is balanced.
//
// https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
//

#include <bits/stdc++.h>

using namespace std;

bool is_balanced(const string& expression)
{
    stack<char> balance;

    for (auto c : expression)
    {
        if (c == '{' || c == '(' || c == '[')
        {
            balance.push(c);
        }
        else if (c == '}' || c == ')' || c == ']')
        {
            // il faut qu'il y ait au moins un bracket ouvrant
            if (balance.empty())
                return false;

            char d = balance.top();
            balance.pop();

            // et que ça soit le bon
            bool ok = (d == '(' && c == ')')
                      || (d == '{' && c == '}')
                      || (d == '[' && c == ']');

            if (! ok)
                return false;
        }
    }

    // s'il reste quelque chose, ce n'est pas bien balancé
    return balance.empty();
}

int main()
{
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string expression;
        cin >> expression;
        bool answer = is_balanced(expression);
        if(answer)
            cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
