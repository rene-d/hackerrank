// Tutorials > 30 Days of Code > Day 12: Inheritance
// Learn about inheritance.
//
// https://www.hackerrank.com/challenges/30-inheritance/problem
//

#include <iostream>
#include <vector>

using namespace std;


class Person{
	protected:
		string firstName;
		string lastName;
		int id;
	public:
		Person(string firstName, string lastName, int identification){
			this->firstName = firstName;
			this->lastName = lastName;
			this->id = identification;
		}
		void printPerson(){
			cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n";
		}

};
// (skeliton_head) ----------------------------------------------------------------------


#include <bits/stdc++.h>

class Student :  public Person{
	private:
		vector<int> testScores;
	public:
        /*
        *   Class Constructor
        *
        *   Parameters:
        *   firstName - A string denoting the Person's first name.
        *   lastName - A string denoting the Person's last name.
        *   id - An integer denoting the Person's ID number.
        *   scores - An array of integers denoting the Person's test scores.
        */
        // Write your constructor here
        Student(const string& firstName, const string& lastName, int identification, const vector<int>& scores) :
            Person(firstName, lastName, identification),
            testScores(scores)
        {}

        /*
        *   Function Name: calculate
        *   Return: A character denoting the grade.
        */
        // Write your function here
		char calculate() const
        {
            int sum = std::accumulate(testScores.begin(), testScores.end(), 0);

            float avg = sum / testScores.size();

            if (avg >= 90) return 'O';
            if (avg >= 80) return 'E';
            if (avg >= 70) return 'A';
            if (avg >= 55) return 'P';
            if (avg >= 40) return 'D';
            return 'T';
        }
};

// (skeliton_tail) ----------------------------------------------------------------------
int main() {
	string firstName;
  	string lastName;
	int id;
  	int numScores;
	cin >> firstName >> lastName >> id >> numScores;
  	vector<int> scores;
  	for(int i = 0; i < numScores; i++){
	  	int tmpScore;
	  	cin >> tmpScore;
		scores.push_back(tmpScore);
	}
	Student* s = new Student(firstName, lastName, id, scores);
	s->printPerson();
	cout << "Grade: " << s->calculate() << "\n";
	return 0;
}
