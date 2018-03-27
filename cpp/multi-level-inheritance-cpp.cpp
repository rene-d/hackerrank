// Multi Level Inheritance 
// Learn what multiple inheritance is and try to solve this problem.
// 
// https://www.hackerrank.com/challenges/multi-level-inheritance-cpp/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Triangle{
	public:
		void triangle(){
			cout<<"I am a triangle\n";
		}
};

class Isosceles : public Triangle{
  	public:
  		void isosceles(){
    		cout<<"I am an isosceles triangle\n";
  		}
};
// (template_head) ----------------------------------------------------------------------

//Write your code here.
class Equilateral : public Isosceles{
     public:
        void equilateral(){
          cout<<"I am an equilateral triangle\n";
        }
};


// (template_tail) ----------------------------------------------------------------------
int main(){
  
    Equilateral eqr;
    eqr.equilateral();
    eqr.isosceles();
    eqr.triangle();
    return 0;
}
