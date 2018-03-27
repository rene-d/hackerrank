// Rectangle Area
// Find out the area of a rectangle. You are given the objects to the class and you have to implement these classes.
// 
// https://www.hackerrank.com/challenges/rectangle-area/problem
// 

#include <iostream>

using namespace std;
// (skeliton_head) ----------------------------------------------------------------------

/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle
{
protected:
    int width;
    int height;
public:
    void display() const
    {
        cout <<  width << " " << height << endl;
    }
    
    void read_input()
    {
        cin >> width >> height;
    }
};

class RectangleArea : public Rectangle
{
public:
    void display() const
    {
        cout <<  (width * height) << endl;
    }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
    /*
     * Declare a RectangleArea object
     */
    RectangleArea r_area;
    
    /*
     * Read the width and height
     */
    r_area.read_input();
    
    /*
     * Print the width and height
     */
    r_area.Rectangle::display();
    
    /*
     * Print the area
     */
    r_area.display();
    
    return 0;
}
