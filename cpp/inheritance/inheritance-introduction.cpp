// Inheritance Introduction
// Learn how to inherit classes from other classes.
// 
// https://www.hackerrank.com/challenges/inheritance-introduction/problem
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
// (template_head) ----------------------------------------------------------------------

class Isosceles : public Triangle{
    public:
    	void isosceles(){
    		cout<<"I am an isosceles triangle\n";
    	}
        //Write your code here.
		void description()
		{
			cout << "In an isosceles triangle two sides are equal" << endl;
		}
};

// (template_tail) ----------------------------------------------------------------------
int main(){
    Isosceles isc;
    isc.isosceles();
  	isc.description();
    isc.triangle();
    return 0;
}