// C > Arrays and Strings > Printing Tokens
// Given a sentence, print each word in a new line.
//
// https://www.hackerrank.com/challenges/printing-tokens-/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char s[1001];

    while (scanf("%s", s) == 1)
    {
        printf("%s\n", s);
    }

    return 0;
}
