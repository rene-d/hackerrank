#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


char A[100000];
int N;


char find(int x, int y)
{
    char Ax = A[x - 1];
    if (x == y) return Ax;
    if (Ax % 2 == 1) return 1;          // odd^b toujours odd

    char p = 1;

    for (int i = y; i >= x; --i)
    {
        if (p == 0) p = 1;              // a^0  
        else if (A[i] == 0) p = 0;      // 0^b b≠0
        else p = 1;
    }

    if (p == 0) return 1;
    return Ax;
}


char find_opti(int x, int y)
{
    if (x != y && (x < N) && A[x] == 0)
        return 1;
    else
        return A[x - 1];
}


int main() 
{
    int     N, Q, x, y;
    char    *buf = new char[210000];
    char    *end;

    fgets(buf, 10, stdin);
    N = (int) strtol(buf, NULL, 10);

    fgets(buf, 210000, stdin);
    end = buf;
    for (int i = 0; i < N; ++i)
    {
        //A[i] = (int) strtol(end, &end, 10);
        //end += 1;
        
        // optimisé
        A[i] = buf[i * 2] - '0';
    }

    fgets(buf, 10, stdin);
    Q = (int) strtol(buf, NULL, 10);

    for (int i = 0; i < Q; ++i)
    {
        fgets(buf, 15, stdin);
        x = (int) strtol(buf, &end, 10);
        y = (int) strtol(end + 1, NULL, 10);

        puts(find_opti(x, y) % 2 ? "Odd" : "Even");
    }

    delete[] buf;

    return 0;   
}
