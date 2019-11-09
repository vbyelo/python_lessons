class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return Complex(real=self.real + other.real, imag=self.imag + other.imag)


if __name__ == "__main__":
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    print(c1)
    print(c2)
    c3 = c1 + c2
    print(c3)
