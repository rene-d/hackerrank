// C > Conditionals and Loops > Bitwise Operators
// Apply everything we've learned in this bitwise operators' challenge.
//
// https://www.hackerrank.com/challenges/bitwise-operators-in-c/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k)
{
  //Write your code here.
    int max_and = 0, max_or = 0, max_xor = 0;

    for (int a = 1; a < n; ++a)
    {
        for (int b = a + 1; b <= n; ++b)
        {
            int x;

            x = a & b; if (x < k && x > max_and) max_and = x;
            x = a | b; if (x < k && x > max_or) max_or = x;
            x = a ^ b; if (x < k && x > max_xor) max_xor = x;
        }
    }

    printf("%d\n", max_and);
    printf("%d\n", max_or);
    printf("%d\n", max_xor);
}

int main()
{
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}
