// Tutorials > 10 Days of Javascript > Day 4: Create a Rectangle Object
// Create an object with certain properties in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-objects/problem
// challenge id: 21012
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
 * Complete the Rectangle function
 */
function Rectangle(a, b) {

    return {
        length: a,
        width: b,
        perimeter: (a + b) * 2,
        area: a * b
    };
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const a = +(readLine());
    const b = +(readLine());

    const rec = new Rectangle(a, b);

    console.log(rec.length);
    console.log(rec.width);
    console.log(rec.perimeter);
    console.log(rec.area);
}
