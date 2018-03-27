// Box It!
//
// https://www.hackerrank.com/challenges/box-it/problem

//#include<bits/stdc++.h>
#include <iostream>

using namespace std;



//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box
{
    int l, b, h;

public:
    Box() : l(0), b(0), h(0)
    {}
    
    Box(int length, int breadth, int height) : l(length), b(breadth), h(height)
    {}

    int getLength() const 
    { 
        return l; 
    }

    int getBreadth() const
    {
        return b;
    }

    int getHeight() const
    {
        return h;
    }

    long long CalculateVolume() const
    {
        return (long long)l * (long long)b * (long long) h;
    }

    bool operator<(const Box& r) const
    {
        return l < r.l 
              || (l == r.l && b < r.b)
              || (l == r.l && b == r.b && h < r.h);
    }
};

ostream& operator<<(ostream& out, const Box& B)
{
    out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight();
    return out;
}







void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
    return 0;
}