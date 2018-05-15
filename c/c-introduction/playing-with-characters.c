// C > Introduction > Playing With Characters
// input character, string and a sentence
//
// https://www.hackerrank.com/challenges/playing-with-characters/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LEN 100

int main()
{
    char ch;
    char s[MAX_LEN];

    scanf("%c", &ch);
    printf("%c\n", ch);

    scanf("%s", s);
    printf("%s\n", s);
    scanf("\n");

    fgets(s, MAX_LEN, stdin);
    printf("%s", s);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}