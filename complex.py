import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return Complex(real=self.real + other.real, imag=self.imag + other.imag)

    def __sub__(self, other):
        return Complex(real=self.real - other.real, imag=self.imag - other.imag)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __mul__(self, other):
        return Complex(
            real=self.real * other.real - self.imag * other.imag,
            imag=self.real * other.imag + self.imag * other.real,
        )

if __name__ == "__main__":

    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    print(str(c1), c1.__abs__())
    print(c2, abs(c2))
    c3 = c1 + c2
    print(c3, abs(c3))

    c4 = c1 * c2
    print(c4, abs(c4))

    i1 = Complex(0, 1)
    print("imaginary one", i1)
    m1 = i1 * i1
    print(m1)
