// C > Functions > Sorting Array of Strings
//
//
// https://www.hackerrank.com/challenges/sorting-array-of-strings/problem
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// (skeliton_head) ----------------------------------------------------------------------

int lexicographic_sort(const char* a, const char* b)
{
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b)
{
    return strcmp(b, a);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b)
{
    int distincts[256];
    int d1 = 0, d2 = 0;

    memset(distincts, 0, sizeof(distincts));
    for (const char *i = a; *i; ++i) distincts[*i] = 1;
    for (int i = 0; i < 128; ++i) d1 += distincts[i];

    memset(distincts, 0, sizeof(distincts));
    for (const char *i = b; *i; ++i) distincts[*i] = 1;
    for (int i = 0; i < 128; ++i) d2 += distincts[i];

    if (d1 != d2) return d1 - d2;
    return strcmp(a, b);
}

int sort_by_length(const char* a, const char* b)
{
    int d = strlen(a) - strlen(b);
    if (d != 0) return d;
    return strcmp(a, b);
}

void string_sort(char** arr,  int len, int (*cmp_func)(const char* a, const char* b))
{
    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (cmp_func(arr[i], arr[j]) > 0)
            {
                char *tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}

// (skeliton_tail) ----------------------------------------------------------------------
int main()
{
    int n;
    scanf("%d", &n);

    char** arr;
	arr = (char**)malloc(n * sizeof(char*));

    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");
}
