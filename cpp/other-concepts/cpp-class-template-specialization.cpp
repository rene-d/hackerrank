// C++ Class Template Specialization
// Class templates in C++ create specializations for certain types.  These can be used when difficult to provide a generic implementation.
//
// https://www.hackerrank.com/challenges/cpp-class-template-specialization/problem
//

#include <iostream>
using namespace std;
enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };

template <typename T> struct Traits;
// (skeliton_head) ----------------------------------------------------------------------

// Define specializations for the Traits class template here.

template<>
struct Traits<Color>
{
 public:
    static string name(int i)
    {
        if (i == (int) Color::red) return "red";
        if (i == (int) Color::green) return "green";
        if (i == (int) Color::orange) return "orange";
        return "unknown";
    }
};


template<>
struct Traits<Fruit>
{
 public:
    static string name(int i)
    {
        if (i == (int) Fruit::apple) return "apple";
        if (i == (int) Fruit::orange) return "orange";
        if (i == (int) Fruit::pear) return "pear";
        return "unknown";
    }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
	int t = 0; std::cin >> t;

    for (int i=0; i!=t; ++i) {
        int index1; std::cin >> index1;
        int index2; std::cin >> index2;
        cout << Traits<Color>::name(index1) << " ";
        cout << Traits<Fruit>::name(index2) << "\n";
    }
}
