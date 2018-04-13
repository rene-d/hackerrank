// Tutorials > 30 Days of Code > Day 13: Abstract Classes
// Build on what you've already learned about Inheritance with this Abstract Classes challenge
//
// https://www.hackerrank.com/challenges/30-abstract-classes/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class Book{
    protected:
        string title;
        string author;
    public:
        Book(string t,string a){
            title=t;
            author=a;
        }
        virtual void display()=0;

};
// (skeliton_head) ----------------------------------------------------------------------

class MyBook : public Book
{
    int price;
public:
    //   Class Constructor
    //
    //   Parameters:
    //   title - The book's title.
    //   author - The book's author.
    //   price - The book's price.
    //
    MyBook(const string& t, const string& a, int p) : Book(t, a), price(p)
    {
    }

    //   Function Name: display
    //   Print the title, author, and price in the specified format.
    //
    virtual void display() override
    {
        cout << "Title: " << this->Book::title << endl;
        cout << "Author: " << this->Book::author << endl;
        cout << "Price: " << price << endl;
    }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main() {
    string title,author;
    int price;
    getline(cin,title);
    getline(cin,author);
    cin>>price;
    MyBook novel(title,author,price);
    novel.display();
    return 0;
}
