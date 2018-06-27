// Tutorials > 10 Days of Javascript > Day 1: Functions
// Practice writing JavaScript functions.
//
// https://www.hackerrank.com/challenges/js10-function/problem
// challenge id: 21019
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

/*
 * Create the function factorial here
 */
function factorial(n)
{
    let f = 1;
    while (n > 1)
    {
        f *= n;
        --n;
    }
    return f;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const n = +(readLine());

    console.log(factorial(n));
}
