// C > Introduction > "Hello World!" in C
// This challenge will help you to learn to input some data and then output some data.
//
// https://www.hackerrank.com/challenges/hello-world-c/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    char s[100];
    scanf("%[^\n]%*c", s);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    puts("Hello, World!");
    puts(s);

    return 0;
}
