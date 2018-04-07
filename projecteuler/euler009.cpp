// Project Euler #9: Special Pythagorean triplet
// A what triplet, you say?
//
// https://www.hackerrank.com/contests/projecteuler/challenges/euler009
//

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    const int M = 3000;
    int cache[M + 1];

    for (int i = 0; i <= M; ++i)
        cache[i] = -1;

    for (int a = 1; a < M; ++a)
    {
        int a_a = a * a;

        for (int b = a + 1; b <= M - a; ++b)
        {
            int c_c = a_a + b * b;

            if (c_c % 4 == 3) continue;

            int c = (int) sqrt(c_c);
            if (c * c != c_c) continue;

            int p = a + b + c;
            if (p > M) break;

            int abc = a * b * c;
            if (cache[p] < abc) cache[p] = abc;
        }
    }

    int t;
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n;
        scanf("%d",&n);


        printf("%d\n", cache[n]);
    }
    return 0;
}
