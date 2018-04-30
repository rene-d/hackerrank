// Classes and Objects
// Familiarize yourself with classes and objects.
//
// https://www.hackerrank.com/challenges/classes-objects/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// (template_head) ----------------------------------------------------------------------

// Write your Student class here
class Student
{
    int score_ = 0 ;
public:
    void input()
    {
        int x;
        score_ = 0;
        for (int i = 0; i < 5; ++i)
        {
            cin >> x;
            score_ += x;
        }
    }
    int calculateTotalScore() const
    { return score_; }
};

// (template_tail) ----------------------------------------------------------------------
int main() {
    int n; // number of students
    cin >> n;
    Student *s = new Student[n]; // an array of n students

    for(int i = 0; i < n; i++){
        s[i].input();
    }

    // calculate kristen's score
    int kristen_score = s[0].calculateTotalScore();

    // determine how many students scored higher than kristen
    int count = 0;
    for(int i = 1; i < n; i++){
        int total = s[i].calculateTotalScore();
        if(total > kristen_score){
            count++;
        }
    }

    // print result
    cout << count;

    return 0;
}
