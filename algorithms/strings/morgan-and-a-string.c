// Morgan and a String
// Find the lexicographically minimal string that can be formed by the combination of two strings.
//
// https://www.hackerrank.com/challenges/morgan-and-a-string/problem
//

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char *morgan;

void morganAndString(const char *a, const char *b) {
    // Complete this function
    char *r = morgan;
    while (*a && *b)
    {
        if (strcmp(a, b) < 0)
        {
            *r++ = *a++;
            if (!*a) { strcpy(r, b); return; }
        }
        else
        {
            *r++ = *b++;
            if (!*b) { strcpy(r, a); return; }
       }

    }
    *r = 0;
}

int main() {
    int t;
    char *a, *b;

    a = (char *)malloc(128000 * sizeof(char));
    b = (char *)malloc(128000 * sizeof(char));
    morgan = (char *)malloc(256000 * sizeof(char));

    scanf("%i", &t);
    for(int a0 = 0; a0 < t; a0++) {
        scanf("%s", a);
        scanf("%s", b);
        strcat(a, "z");
        strcat(b, "z");
        morganAndString(a, b);
        morgan[strlen(a) + strlen(b)-2] = 0;
        printf("%s\n", morgan);
    }

    free(a);
    free(b);
    free(morgan);

    return 0;
}
