// Tutorials > 10 Days of Javascript > Day 7: Regular Expressions III
// Regex
//
// https://www.hackerrank.com/challenges/js10-regexp-3/problem
// challenge id: 21896
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
     * It must match ALL occurrences of numbers in a string.
     */
    const re = /(\d+)/g;

    /*
     * Do not remove the return statement
     */
    return re;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const re = regexVar();
    const s = readLine();

    const r = s.match(re);

    for (const e of r) {
        console.log(e);
    }
}
