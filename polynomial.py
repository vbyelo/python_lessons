#
# https://pl.wikipedia.org/wiki/Wielomian 
# 

import numbers
import numpy as np
import matplotlib.pyplot as plt


class Polynomial:

 

    def __init__(self, coef=[]):
        self.coef = coef

    def __call__(self, x):
        result = 0
        num = len(self.coef)
        for i in range(num):
            result += self.coef[i] * x ** (num - i - 1)
        return result

    def __str__(self):
        result = ""
        num = len(self.coef)

        def get_coef(i, beginning=False, zero_degree=False):

            if self.coef[i] == 0:
                return ""

            if zero_degree:
                value = str(abs(self.coef[i]))
            else:
                value = str(abs(self.coef[i])) if abs(self.coef[i]) != 1 else ""

            sign = "-" if self.coef[i] < 0 else ("+" if not beginning else "")
            return sign + " " + value

        def get_power(i):
            p = num - i - 1
            if p == 0:
                return ""
            elif p == 1:
                return "x"
            else:
                return f"x^{p}"

        for i in range(num):
            v = get_coef(i, i == 0, i == len(self.coef) - 1)
            if v:
                result += v + get_power(i) + " "
        return result

    def __add__(self, other):
        pass

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Polynomial([other*c for c in self.coef])
        else:
            raise ValueError('Polynomial multiplication is not jet implimented')

    __rmul__ = __mul__

if __name__ == "__main__":
    arg = np.linspace(0, 1)

    f2 = Polynomial([1, 2, 13])
    f4 = Polynomial([1, -2, 0, -3, 2])

    _f2 = np.poly1d([1, 2, 13])
    _f4 = np.poly1d([1, -2, 0, -3, 2])

    # plt.plot(arg, f2(arg), label=str(f2))
    # plt.plot(arg, f4(arg), label=str(f4))

    # plt.plot(arg, _f2(arg), ls="-.", label=str(_f2))
    # plt.plot(arg, _f4(arg), ls="-.", label=str(_f4))

    plt.plot(arg, (3 * _f2)(arg), ls="-", label="python function")
    plt.plot(arg, (3 * f2)(arg), ls="-.", label="my function")

    plt.legend()
    plt.show()
