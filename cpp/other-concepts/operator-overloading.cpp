// Operator Overloading
// Learn how to overload operators. Print the sum of two matrices and print the resultant matrix.
// 
// https://www.hackerrank.com/challenges/operator-overloading/problem
// 

#pragma GCC diagnostic ignored "-Wsign-compare"
#pragma GCC diagnostic ignored "-Wsign-conversion"
#pragma GCC diagnostic ignored "-Wshorten-64-to-32"
#pragma GCC diagnostic ignored "-Wunused-variable"
#pragma GCC diagnostic ignored "-Wfloat-conversion"


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// (skeliton_head) ----------------------------------------------------------------------

class Matrix 
{
public:
    vector<vector<int>> a;
    
    Matrix& operator+(const Matrix& r)
    {
        if (a.size() == r.a.size())
        {
            for (size_t i = 0; i < a.size(); ++i)
            {
                auto& ai = a[i];
                const auto& ri = r.a[i];
                if (ai.size() == ri.size())
                {
                    for (size_t j = 0; j < ai.size(); ++j)
                    {
                        ai[j] += ri[j];
                    }

                }
            }
        }
        return *this;
    }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main () {
   int cases,k;
   cin >> cases;
   for(k=0;k<cases;k++) {
      Matrix x;
      Matrix y;
      Matrix result;
      int n,m,i,j;
      cin >> n >> m;
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         x.a.push_back(b);
      }
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         y.a.push_back(b);
      }
      result = x+y;
      for(i=0;i<n;i++) {
         for(j=0;j<m;j++) {
            cout << result.a[i][j] << " ";
         }
         cout << endl;
      }
   }  
   return 0;
}
