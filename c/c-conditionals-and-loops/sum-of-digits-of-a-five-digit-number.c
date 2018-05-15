// C > Conditionals and Loops > Sum of Digits of a Five Digit Number
// to calculate the sum of digits of a five digit number.

//
// https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.

    int sum = 0;
    while (n != 0)
    {
        sum += n % 10;
        n /= 10;
    }
    printf("%d\n", sum);

    return 0;
}
