// Tutorials > 10 Days of Javascript > Day 1: Let and Const
// The const declaration creates a read-only reference to a value.
//
// https://www.hackerrank.com/challenges/js10-let-and-const/problem
// challenge id: 21020
//

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });

    main();
});

function readLine() {
    return inputString[currentLine++];
}
// (skeliton_head) ----------------------------------------------------------------------

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    let radius = Number(readLine());

    const PI = Math.PI;

    // Print the area of the circle:
    let area = PI * radius * radius;
    console.log(area);

    // Print the perimeter of the circle:
    let perimeter = PI * radius * 2;
    console.log(perimeter);

// (skeliton_tail) ----------------------------------------------------------------------
    try {
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
