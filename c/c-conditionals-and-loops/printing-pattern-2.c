// C > Conditionals and Loops > Printing Pattern using Loops
//
//
// https://www.hackerrank.com/challenges/printing-pattern-2/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define max(x,y)        ((x)>(y)?(x):(y))

int main()
{
    int i, j;
    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.

    for (i = 0; i < 2 * n - 1; ++i)
    {
        for (j = 0; j < 2 * n - 1; ++j)
        {
            printf("%d ", max(abs(n - i - 1) + 1, abs(n - j - 1) + 1));
        }
        printf("\n");
    }

    return 0;
}
