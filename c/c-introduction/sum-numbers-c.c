// C > Introduction > Sum and Difference of Two Numbers
// Get started with data types.
//
// https://www.hackerrank.com/challenges/sum-numbers-c/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int i, j;
    float f, g;

    if (scanf("%d %d", &i, &j) == 2 && scanf("%f %f", &f, &g) == 2)
    {
        printf("%d %d\n", i + j, i - j);
        printf("%.1f %.1f\n", f + g, f - g);
    }

    return 0;
}
