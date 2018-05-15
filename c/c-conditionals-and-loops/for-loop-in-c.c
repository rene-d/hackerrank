// C > Conditionals and Loops > For Loop in C
// Learn how to use for loop and print the output as per the given conditions
//
// https://www.hackerrank.com/challenges/for-loop-in-c/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


static const char *digits[] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

int main()
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.

    for (int i = a; i <= b; ++i)
    {
        if (i >= 0 && i < 10)
            printf("%s\n", digits[i]);
        else if (i % 2 == 0)
            printf("even\n");
        else
            printf("odd\n");

    }

    return 0;
}
