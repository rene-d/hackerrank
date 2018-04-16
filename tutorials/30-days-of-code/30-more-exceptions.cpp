// Tutorials > 30 Days of Code > Day 17: More Exceptions
// Throw an exception when user sends wrong parameters to a method.
//
// https://www.hackerrank.com/challenges/30-more-exceptions/problem
//

#include <cmath>
#include <iostream>
#include <exception>
#include <stdexcept>
using namespace std;
// (skeliton_head) ----------------------------------------------------------------------

//Write your code here
class Calculator
{
public:
    int power(int n, int p)
    {
        if (n < 0 || p < 0)
            throw invalid_argument("n and p should be non-negative");

        return pow(n, p);
    }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
    Calculator myCalculator=Calculator();
    int T,n,p;
    cin>>T;
    while(T-->0){
      if(scanf("%d %d",&n,&p)==2){
         try{
               int ans=myCalculator.power(n,p);
               cout<<ans<<endl;
         }
         catch(exception& e){
             cout<<e.what()<<endl;
         }
      }
    }

}
