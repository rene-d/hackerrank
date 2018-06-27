// Tutorials > 10 Days of Javascript > Day 4: Classes
// Practice using JavaScript classes.
//
// https://www.hackerrank.com/challenges/js10-class/problem
// challenge id: 21855
//

/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon {
    constructor(sides) {
        this.sides = sides;
    }

    perimeter()
    {
        let sum = 0;
        for (const s of this.sides)
            sum += s;
        return sum;
    }
}

// (skeliton_tail) ----------------------------------------------------------------------
const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
