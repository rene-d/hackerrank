// C > Arrays and Strings > 1D Arrays in C
// Create an array in c and sum the elements.
//
// https://www.hackerrank.com/challenges/1d-arrays-in-c/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    scanf("%d", &n);

    int *arr = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i)
        scanf("%d", &arr[i]);

    int sum = 0;
    for (int i = 0; i < n; ++i)
        sum += arr[i];

    printf("%d\n", sum);

    free(arr);

    return 0;
}
