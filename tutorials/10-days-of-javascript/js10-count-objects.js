// Tutorials > 10 Days of Javascript > Day 4: Count Objects
// Iterate over the elements in an array and perform an action based on each element's properties.
//
// https://www.hackerrank.com/challenges/js10-count-objects/problem
// challenge id: 21013
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
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 *
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {

    var count = 0;
    for (const o of objects)
        if (o.x == o.y) count++;

    return count;
}

// (skeliton_tail) ----------------------------------------------------------------------
function main() {
    const n = +(readLine());
    let objects = [];

    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');

        objects.push({x: +(a), y: +(b)});
    }

    console.log(getCount(objects));
}
