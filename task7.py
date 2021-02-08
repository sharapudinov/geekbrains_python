class Complex:

    @staticmethod
    def zero():
        return Complex()

    @staticmethod
    def i():
        return Complex(0, 1)

    @staticmethod
    def one():
        return Complex(1, 0)

    def __init__(self, a=0, b=0):
        self._a = a
        self._b = b

    def __add__(self, other):
        return Complex(self._a + other._a, self._b + other._b)

    def __sub__(self, other):
        return Complex(self._a - other._a, self._b - other._b)

    def __mul__(self, other):
        return Complex(self._a * other._a - self._b * other._b, self._a * other._b + self._b * other._a)

    def __neg__(self):
        return Complex(-self._a, -self._b)

    def __pos__(self):
        return self

    def __str__(self):
        return str((self._a, self._b))


z = Complex(3, 4)
i = Complex.i()
one = Complex.one()
zero = Complex.zero()

print(one * i)
print(one + z)
print(zero * z)
print(z * z)
print(z * i)
print(-z)
print(i * i)
