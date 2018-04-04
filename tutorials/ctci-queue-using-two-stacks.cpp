// Queues: A Tale of Two Stacks
// Create a queue data structure using two stacks.
// 
// https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
// 

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

class MyQueue {
  
    public:
        stack<int> stack_newest_on_top, stack_oldest_on_top;  

        void push(int x) 
        {
            // dans cette stack, les éléments sont ordonnés selon leur ordre d'arrivée
            stack_newest_on_top.push(x);
        }

        void pop() 
        {
            // dans l'autre stack, les éléments sont ordonnés selon leur ordre INVERSE d'arrivée
            if (stack_oldest_on_top.empty())
            {
                while (! stack_newest_on_top.empty())
                {
                    int x = stack_newest_on_top.top();
                    stack_newest_on_top.pop();
                    stack_oldest_on_top.push(x);
                }
            }
            stack_oldest_on_top.pop();
        }

        int front() 
        {
            int x = -1;
            if (stack_oldest_on_top.empty())
            {
                while (! stack_newest_on_top.empty())
                {
                    x = stack_newest_on_top.top();
                    stack_newest_on_top.pop();
                    stack_oldest_on_top.push(x);

                }
            }
            else
            {
                x = stack_oldest_on_top.top();
            }
            return x;
        }
    
};

int main() {
    MyQueue q1;
    int q, type, x;
    cin >> q;
    
    for(int i = 0; i < q; i++) {
        cin >> type;
        if(type == 1) {
            cin >> x;
            q1.push(x);
        }
        else if(type == 2) {
            q1.pop();
        }
        else cout << q1.front() << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
