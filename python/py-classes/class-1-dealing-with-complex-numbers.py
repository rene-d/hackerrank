# Python > Classes > Classes: Dealing with Complex Numbers
# Create a new data type for complex numbers.
#
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
#

import math
# (skeliton_head) ----------------------------------------------------------------------

class Complex(object):
    def __init__(self, real, imaginary):
        self.a = real
        self.b = imaginary

    def __add__(self, no):
        return Complex(self.a + no.a, self.b + no.b)

    def __sub__(self, no):
        return Complex(self.a - no.a, self.b - no.b)

    def __mul__(self, no):
        # (a+ib)(c+id) = (ac-bd) + (ad+bc)i
        return Complex(self.a * no.a - self.b * no.b, self.a * no.b + self.b * no.a)

    def __truediv__(self, no):
        # (a+ib)/(c+id) = (a+ib)*(c-id)   /((c+id)(c-id))
        #               = (ac+bd+(bc-ad)i)/(c*c+d*d)
        x = no.a ** 2 + no.b ** 2
        return Complex((self.a * no.a + self.b * no.b) / x, (self.b * no.a - self.a * no.b) / x)

    def mod(self):
        return Complex(math.sqrt(self.a ** 2 + self.b ** 2), 0)

    def __str__(self):
        if self.b == 0:
            result = "%.2f+0.00i" % (self.a)
        elif self.a == 0:
            if self.b >= 0:
                result = "0.00+%.2fi" % (self.b)
            else:
                result = "0.00-%.2fi" % (abs(self.b))
        elif self.b > 0:
            result = "%.2f+%.2fi" % (self.a, self.b)
        else:
            result = "%.2f-%.2fi" % (self.a, abs(self.b))
        return result

# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
