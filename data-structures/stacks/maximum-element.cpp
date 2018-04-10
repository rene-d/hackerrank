// Maximum Element
// Given three types of queries, insert an element, delete an element or find the maximum element in a stack.
//
// https://www.hackerrank.com/challenges/maximum-element/problem
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

 // nota: le challenge garantit que les bornes ne seront jamais dépassées
 // ainsi, on ne vérifie rien sur la validité des données en entrée


int stack[100000];
int top = 0;


// Solution 1: naïve

int main_naif()
{
    int q;
    cin >> q;
    while (q--)
    {
        int op;
        cin >> op;

        if (op == 1)
        {
            int x;
            cin >> x;
            //push

            stack[top++] = x;
        }
        else if (op == 2)
        {
            //delete
            top--;
        }
        else if (op == 3)
        {
            //print max
            int max = -1;
            for (int i = 0; i < top; ++i)
                if (stack[i] > max) max = stack[i];
            cout << max << endl;
        }
    }
    return 0;
}


// Solution 2: performante
// pas la peine de stacker les éléments, il n'y a que le max qui nous intéresse!

int main()
{
    int q;
    cin >> q;
    while (q--)
    {
        int op;
        cin >> op;

        if (op == 1)
        {
            int x;
            cin >> x;
            //push

            // par défaut le max de la stack est l'élément lu
            int m = x;

            // s'il y a qqch dans la stack, on vérifie le max
            if (top > 0)
            {
                if (stack[top - 1] > m) m = stack[top - 1];
            }

            stack[top++] = m;
        }
        else if (op == 2)
        {
            //delete
            top--;
        }
        else if (op == 3)
        {
            //print max
            cout << stack[top - 1] << endl;
        }
    }
    return 0;
}
