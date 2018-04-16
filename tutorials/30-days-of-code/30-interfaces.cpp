// Tutorials > 30 Days of Code > Day 19: Interfaces
// Welcome to Day 19! Learn about interfaces in this challenge!
//
// https://www.hackerrank.com/challenges/30-interfaces/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class AdvancedArithmetic{
    public:
        virtual int divisorSum(int n)=0;
};
// (skeliton_head) ----------------------------------------------------------------------


class Calculator : public AdvancedArithmetic
{
public:
    virtual int divisorSum(int n) override
    {
        int sum = 0;
        int r = (int) sqrt(n);
        for (int i = 1; i <= n; ++i)
        {
            if (n % i == 0) sum += i;
        }
        return sum;
    }
};


// (skeliton_tail) ----------------------------------------------------------------------
int main(){
    int n;
    cin >> n;
    AdvancedArithmetic *myCalculator = new Calculator();
    int sum = myCalculator->divisorSum(n);
    cout << "I implemented: AdvancedArithmetic\n" << sum;
    return 0;
}
