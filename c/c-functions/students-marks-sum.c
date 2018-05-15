// C > Functions > Students Marks Sum
// An easy challenge on pointers
//
// https://www.hackerrank.com/challenges/students-marks-sum/problem
//

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// (skeliton_head) ----------------------------------------------------------------------

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender)
{
    int sum = 0;

    for (int i = gender == 'b' ? 0 : 1; i < number_of_students; i += 2)
    {
        sum += marks[i];
    }
    return sum;
}

// (skeliton_tail) ----------------------------------------------------------------------
int main() {
    int number_of_students;
    char gender;
    int sum;

    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));

    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }

    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);

    return 0;
}
