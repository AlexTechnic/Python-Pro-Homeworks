""" 2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання, віднімання та
множення для екземплярів цього класу. """

import math


class RationalNum:

    def __init__(self, a: int, b=1):
        """
        Class represent fraction number (1/2, 3/10, etc), supporting operations == != > >= <= + * with instances.
        :param a: numerator
        :param b: denominator
        """
        if not isinstance(a, int):
            raise TypeError('Error: must be int type')
        if not isinstance(b, int):
            raise TypeError('Error: must be int type')
        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    def __eq__(self, other):
        k = math.gcd(self.__a, self.__b)
        self.__a //= k
        self.__b //= k

        k = math.gcd(other.__a, other.__b)
        other.__a //= k
        other.__b //= k
        return (self.__a, self.__b) == (other.__a, other.__b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.__a / self.__b > other.__a / other.__b

    def __lt__(self, other):
        return self.__a / self.__b < other.__a / other.__b

    def __sub__(self, other):
        b = self.__b * other.__b
        a = b // self.__b * self.__a -\
            b // other.__b * other.__a
        return RationalNum(a, b)

    def __rsub__(self, other):
        b = self.__b * other.__b
        a = b // self.__b * self.__a -\
            b // other.__b * other.__a
        return RationalNum(a, b)

    def __isub__(self, other):
        sign = 1 if self.__a * self.__b > 0 else -1
        b = abs(self.__b) * abs(other.__b)
        a = b // abs(self.__b) * abs(self.__a) -\
            b // abs(other.__b) * abs(other.__a)
        self.__a = sign * a
        self.__b = b
        return self

    def __ge__(self, other):
        return self.__a / self.__b >= other.__a / other.__b

    def __le__(self, other):
        return self.__a / self.__b <= other.__a / other.__b

    def __mul__(self, other):
        b = self.__b * other.__b
        a = self.__a * other.__a
        return RationalNum(a, b)

    def __add__(self, other):
        b = self.__b * other.__b
        a = self.__a * other.__b + other.__a * self.__b
        return RationalNum(a, b)

    def __str__(self):
        sign = '' if self.__a * self.__b >= 0 else '-'
        a, b = abs(self.__a), abs(self.__b)
        k = math.gcd(a, b)
        a //= k
        b //= k

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a % b}/{b}'
        return f'{sign}{a}/{b}'


x = RationalNum(1, 2)  # represent rational num 1/2
y = RationalNum(1, 5)  # represent rational num 1/5

print(f'\nx rational num: {x}')
print(f'y rational num: {y} \n')

# add and sub operations
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{y} + {x} = {y + x}')
print(f'{y} - {x} = {y - x} \n')

# greater and less ops
print(f'{x} > {y} ? {x > y}')
print(f'{x} < {y} ? {x < y} \n')

# ge and le ops
print(f'{x} >= {y} ? {x >= y}')
print(f'{x} <= {y} ? {x <= y} \n')

# multiple ops
print(f'{y} * {x} = {y * x}')
print(f'{x} * {y} = {x * y} \n')