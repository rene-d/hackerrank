// Maps-STL
// Learn to use map container. Given some queries, add the marks to a corresponding student, delete a student  and print the marks of a particular student.
// 
// https://www.hackerrank.com/challenges/cpp-maps/problem
// 

#include <string>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int     n;
    map<string, int>    students;
    string  name;
    int     mark;
    int     cmd;
    
    cin >> n;
    while (n-- != 0)
    {
        cin >> cmd;
        if (cmd == 1) { cin >> name >> mark; students[name] += mark; }
        else if (cmd == 2) { cin >> name; students.erase(name); }
        else if (cmd == 3) { cin >> name; cout << students[name] << endl; }
    }
    
    return 0;
}

