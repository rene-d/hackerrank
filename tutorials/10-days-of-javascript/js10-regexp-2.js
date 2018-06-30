// Tutorials > 10 Days of Javascript > Day 7: Regular Expressions II
// Write a JavaScript RegExp to match a name satisfying certain criteria.
//
// https://www.hackerrank.com/challenges/js10-regexp-2/problem
// challenge id: 21850
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
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.',
     * followed by one or more letters.
     */
    const re = /^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.).+/;

    /*
     * Do not remove the return statement
     */
    return re;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const re = regexVar();
    const s = readLine();

    console.log(!!s.match(re));
}
