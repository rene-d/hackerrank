// Tutorials > 10 Days of Javascript > Day 1: Arithmetic Operators
// Learn arithmetic operators in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem
// challenge id: 21011
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
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;

    area = length * width;

    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;

    perimeter = (length + width) * 2;

    return perimeter;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const length = +(readLine());
    const width = +(readLine());

    console.log(getArea(length, width));
    console.log(getPerimeter(length, width));
}
