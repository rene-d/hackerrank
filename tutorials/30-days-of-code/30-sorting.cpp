// Tutorials > 30 Days of Code > Day 20: Sorting
// Find the minimum number of conditional checks taking place in Bubble Sort
//
// https://www.hackerrank.com/challenges/30-sorting/problem
//

    #include <cmath>
    #include <cstdio>
    #include <vector>
    #include <iostream>
    #include <algorithm>
    using namespace std;


    int main()
    {
        int n;
        vector<int> arr;

        cin >> n;

        arr.resize(n);
        for (int i = 0; i < n; ++i) cin >> arr[i];

        int swaps = 0;
        bool swapped;
        do {
            swapped = false;
            for (int i = 0; i < n - 1; ++i)
            {
                if (arr[i] > arr[i + 1])
                {
                    swap(arr[i], arr[i + 1]);
                    swaps++;            // compteur de swap
                    swapped = true;     // on devra recommencer...
                }
            }
        } while (swapped);

        cout << "Array is sorted in " << swaps << " swaps." << endl;
        cout << "First Element: " << arr[0] << endl;
        cout << "Last Element: " << arr[n - 1] << endl;

        return 0;
    }
