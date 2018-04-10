// Day 0: Hello, World.
// Practice reading from stdin and printing to stdout.
// 
// https://www.hackerrank.com/challenges/30-hello-world/problem
// 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
// (skeliton_head) ----------------------------------------------------------------------

int main() {
    // Declare a variable named 'input_string' to hold our input.
    char input_string[105]; 
    
    // Read a full line of input from stdin and save it to our variable, input_string.
    scanf("%[^\n]", input_string); 
    
    // Print a string literal saying "Hello, World." to stdout using printf.
    printf("Hello, World.\n");
    
    // TODO: Write a line of code here that prints the contents of input_string to stdout.
    printf("%s\n", input_string);

    return 0;
}
