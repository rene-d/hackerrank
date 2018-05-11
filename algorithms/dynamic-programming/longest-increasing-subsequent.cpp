// The Longest Increasing Subsequence
// Find the length of the longest increase subsequence in a given array.
//
// https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem
//

#include <bits/stdc++.h>
using namespace std;


// C++ implementation to find longest increasing subsequence
// in O(n Log n) time.


// Binary search
int GetCeilIndex(int arr[], vector<int> &T, int l, int r,
                int key)
{
    while (r - l > 1)
    {
        int m = l + (r - l)/2;
        if (arr[T[m]] >= key)
            r = m;
        else
            l = m;
    }

    return r;
}

int LongestIncreasingSubsequence(int arr[], int n)
{
    // Add boundary case, when array n is zero
    // Depend on smart pointers

    vector<int> tailIndices(n, 0); // Initialized with 0
    vector<int> prevIndices(n, -1); // initialized with -1

    int len = 1; // it will always point to empty location
    for (int i = 1; i < n; i++)
    {
        if (arr[i] < arr[tailIndices[0]])
        {
            // new smallest value
            tailIndices[0] = i;
        }
        else if (arr[i] > arr[tailIndices[len - 1]])
        {
            // arr[i] wants to extend largest subsequence
            prevIndices[i] = tailIndices[len - 1];
            tailIndices[len++] = i;
        }
        else
        {
            // arr[i] wants to be a potential condidate of
            // future subsequence
            // It will replace ceil value in tailIndices
            int pos = GetCeilIndex(arr, tailIndices, -1,
                                   len - 1, arr[i]);

            prevIndices[i] = tailIndices[pos - 1];
            tailIndices[pos] = i;
        }
    }

    return len;
}


int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    int result = LongestIncreasingSubsequence(&arr.at(0), arr.size() );
    cout << result << endl;
    return 0;
}
