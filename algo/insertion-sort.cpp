// Insertion Sort Advanced Analysis
// How many shifts will it take Insertion Sort to sort an array?
//
// https://www.hackerrank.com/challenges/insertion-sort/problem
//

#include <iostream>
using namespace std;

const int N = 10000000;
int cnt[N + 1];

void add(int v)
{
    while (v <= N)
    {
        cnt[v]++;
        v += v & -v;
    }
}

int get(int v)
{
    int sum = 0;
    while (v)
    {
        sum += cnt[v];
        v -= v & -v;
    }
    return sum;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;

        long long changes = 0;
        for (int i = 0; i < n; i++)
        {
            int a;
            cin >> a;

            int cnt_larger = get(N) - get(a);
            changes += cnt_larger;

            add(a);
        }

        cout << changes << endl;

        for (int i = 0; i <= N; i++)
            cnt[i] = 0;
    }

    return 0;
}