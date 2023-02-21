""" Module of student subclass based on human class"""

import human


class Student(human.Human):

    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)
        self.grade = grade

    def __str__(self):
        return f'{self.name} {self.surname}, age {self.age} (grade {self.grade})'
