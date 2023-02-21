"""1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння прямокутників за
площею. Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ
прямокутників, які ви складаєте). Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового
прямокутника в n разів)."""


from decimal import Decimal as dec


class Rect:

    def __init__(self, a: int, b: int):
        """
        Class represent rectangle with sides A (width) * B (height), calculates rectangle square S = cm^2,
        support operations > < >= <= + * with instances that calculates by S value.

        Parameters
        ----------
        'a' - width in cm.
        'b' - height in cm.
        """
        self.a = a
        self.b = b

    def rect_area(self) -> int:
        return self.a * self.b

    def __gt__(self, other):
        return self.rect_area() > other.rect_area()

    def __lt__(self, other):
        return self.rect_area() < other.rect_area()

    def __ge__(self, other):
        return self.rect_area() >= other.rect_area()

    def __le__(self, other):
        return self.rect_area() <= other.rect_area()

    def __add__(self, other):
        if isinstance(other, Rect):
            return self.rect_area() + other.rect_area()
        if isinstance(other, int):
            return self.rect_area() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.rect_area() + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.a *= other**0.5
            self.b *= other**0.5
            new_rectangle = Rect(self.a, self.b)
            return new_rectangle
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            self.a *= other**0.5
            self.b *= other**0.5
            new_rectangle = Rect(self.a, self.b)
            return new_rectangle
        return NotImplemented

    def __round__(self, other):
        if isinstance(other, (int, float)):
            self.a = round(self.a, other)
            self.b = round(self.b, other)
            new_rectangle = Rect(self.a, self.b)
            return new_rectangle
        return NotImplemented

    def __str__(self):
        return f'{self.a} x {self.b}'


# creating some rectangles instances
x = Rect(20, 30)
y = Rect(30, 40)

print('\nOperations with rectangles:\n')

# rectangles dimensions and S
print(f'Rectangle X dimensions: {x} cm, S = {x + 0} cm^2')
print(f'Rectangle Y dimensions: {y} cm, S = {y + 0} cm^2 \n')

# greater and less operations of rectangles S
print(f'Rectangle X > Y? {x > y}')
print(f'Rectangle X < Y? {x < y} \n')

# greater than and less than operations of rectangles S
print(f'Rectangle X >= Y? {x >= y}')
print(f'Rectangle X <= Y? {x <= y} \n')

# add operation of rectangles S
print(f'Rectangle X + Y  S = {x + y} cm^2 \n')

# multiple and round operations of rectangles S
print(f'Rectangle X * 10 = {x * 10} cm, S = {round(x + 0)} cm^2')
print(f'Rectangle Y * 10 = {y * 10} cm, S = {round(y + 0)} cm^2 \n')
