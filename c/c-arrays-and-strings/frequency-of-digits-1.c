// C > Arrays and Strings > Digit Frequency
// Given a very large number, count the frequency of each digit from [0-9]
//
// https://www.hackerrank.com/challenges/frequency-of-digits-1/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char s[1001];
    int freq[10] = { 0 };

    scanf("%s", s);

    for (char *c = s; *c; c++)
    {
        if (*c >= '0' && *c <= '9')
        {
            freq[*c - '0']++;
        }
    }

    for (int i = 0; i < 10; i++)
        printf("%d ", freq[i]);

    return 0;
}
