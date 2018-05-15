// C > Arrays and Strings > Array Reversal
// Given an array, reverse it.
//
// https://www.hackerrank.com/challenges/reverse-array-c/problem
//

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }


    /* Write the logic to reverse the array. */
    for (int i = 0; i < num / 2; ++i)
    {
        int tmp = arr[i];
        arr[i] = arr[num - i - 1];
        arr[num - i - 1] = tmp;
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));

    free(arr);

    return 0;
}
