// Tutorials > 10 Days of Javascript > Day 3: Try, Catch, and Finally
// Learn to use `try`, `catch`, and 'finally' in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
// challenge id: 20997
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
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {

    try {
        s = s.split("").reverse().join("");
    }
    catch (e) {
        console.log(e.message);
    }
    finally {
        console.log(s);
    }
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const s = eval(readLine());

    reverseString(s);
}
