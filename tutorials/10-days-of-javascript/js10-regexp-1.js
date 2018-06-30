// Tutorials > 10 Days of Javascript > Day 7: Regular Expressions I
// Get started with Regular Expressions in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-regexp-1/problem
// challenge id: 20996
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

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */

    var re = /^([aeiou]).*\1$/;

    /*
     * Do not remove the return statement
     */
    return re;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const re = regexVar();
    const s = readLine();

    console.log(re.test(s));
}
