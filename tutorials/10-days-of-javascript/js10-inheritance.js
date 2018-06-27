// Tutorials > 10 Days of Javascript > Day 5: Inheritance
// Practice using prototypes and implementing inheritance in JavaScript.
//
// https://www.hackerrank.com/challenges/js10-inheritance/problem
// challenge id: 21000
//

class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}
// (skeliton_head) ----------------------------------------------------------------------

/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */
Rectangle.prototype.area = function() {
    return this.w * this.h;
}

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle {
    constructor(w) {
        super(w, w);
    }
}

// (skeliton_tail) ----------------------------------------------------------------------
if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);

    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}
