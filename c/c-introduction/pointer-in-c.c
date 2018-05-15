// C > Introduction > Pointers in C
// Learn how to declare pointers and use them.
//
// https://www.hackerrank.com/challenges/pointer-in-c/problem
//

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function

    int s = *a + *b;
    int d = *a - *b;
    if (d < 0) d = -d;
    *a = s;
    *b = d;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
