// Tutorials > 10 Days of Javascript > Day 2: Loops
// Learn For, While and Do-While loops in Javascript.
//
// https://www.hackerrank.com/challenges/js10-loops/problem
// challenge id: 20995
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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {

    // syntax 1
    for (var i = 0; i < s.length; ++i)
        if ("aeuio".indexOf(s[i]) >= 0)
            console.log(s[i]);

    // syntax 2
    for (const c of s)
        if ("aeuio".indexOf(c) == -1)
            console.log(c);
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const s = readLine();

    vowelsAndConsonants(s);
}
