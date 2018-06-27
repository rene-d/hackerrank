// Tutorials > 10 Days of Javascript > Day 2: Conditional Statements: If-Else
// Learning about conditional statements.
//
// https://www.hackerrank.com/challenges/js10-if-else/problem
// challenge id: 21009
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

function getGrade(score) {
    let grade;
    // Write your code here

    if (score <= 30 && score >= 0)
        grade = 'FEDCBA'[Math.floor(score / 5)];
    else
        grade = '?';

    return grade;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}
