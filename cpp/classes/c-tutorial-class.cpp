// Class
// Learn how to create and use classes. 
// 
// https://www.hackerrank.com/challenges/c-tutorial-class/problem
//

#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student
{
    int age = 0;
    int standard = 0;
    string first_name, last_name;
public:
    void set_first_name(const string& s) { first_name = s; }
    const string& get_first_name() const { return first_name; }

    void set_last_name(const string& s) { last_name = s; }
    const string& get_last_name() const { return last_name; }

    void set_age(int s) { age = s; }
    int get_age() const { return age; }

    void set_standard(int s) { standard = s; }
    int get_standard() const { return standard; }
    
    string to_string() const
    {
        stringstream ss;
        ss << age << "," << first_name << "," << last_name << "," << standard;
        return ss.str();
    }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
