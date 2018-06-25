// Tutorials > 10 Days of Javascript > Day 3: Arrays
// Output the 2nd largest number in an array in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-arrays/problem
// challenge id: 21014
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

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Editorial is almost unworthy of computer science :/
    let m = 0;
    let mm = 0;
    for (const i of nums) {
        if (i > mm) { m = mm; mm = i; }
        else if (i != mm && i > m) { m = i; }
    }
    return m;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);

    console.log(getSecondLargest(nums));
}
