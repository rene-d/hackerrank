// https://www.hackerrank.com/challenges/deque-stl/problem

#include <iostream>
#include <deque>
#include <algorithm>
#include <sstream>

using namespace std;


void printKMax_basic(int arr[], int n, int k)
{
   //Write your code here.
    std::deque<int> q;

    for (int i = 0; i < n; ++i)
    {
        int a = arr[i];

        q.push_back(a);

        while (q.size() > k) q.pop_front();

        if (q.size() == k)
        {
            int m =  *max_element(q.begin(), q.end());
            cout << m << " ";
        }
    }
    cout << endl;
}


void printKMax(int arr[], int n, int k)
{
   deque<int> dq;

    for (int i=0; i<n; i++){

        // base case for first element
        if (dq.empty()){
            dq.push_back(i);
        }

        // remove elements outside the current window
        if (dq.front() <= (i - k)){
            dq.pop_front();
        }

        // move max element to the front
        while (!dq.empty() && arr[i] >= arr[dq.back()]){
            dq.pop_back();
        }

        dq.push_back(i);

        // print out only when the first window is completed
        if (i >= (k - 1)) {
            cout << arr[dq.front()] << " ";
        }
    }
    cout << endl;
}


int main()
{
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
