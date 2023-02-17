"""
1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).

2. На його основі створіть клас Студент (перевизначте метод виведення інформації).

3. Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи додавання,
видалення студента та метод пошуку студента за прізвищем.  Визначте для Групи метод str() для повернення списку
студентів у вигляді рядка. """


class Human:
    """

    """
    def __init__(self, name='<Name>', surname='<Surname>', born='<in format "YYYY.MM.DD">',
                 cellphone='<in format "+XXXXXXXXXXX">', email='<in format "mail@mail.com">'):

        self.name = name
        self.surname = surname
        self.born = born
        self.cellphone = cellphone
        self.email = email

    def __str__(self):
        return f'\nName: {self.name}' \
               f'\nsurname: {self.surname}' \
               f'\nBorn: {self.born}' \
               f'\nCellphone: {self.cellphone}' \
               f'\nEmail: {self.email}'


class Student(Human):

    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade = grade

    def __str__(self):
        return f'student {self.name} {self.surname} (grade {self.grade})'


class Group:
    def __init__(self):
        self.__title = 'Empty title'
        self.__max_members = 99
        self.__members = []

    def get_max_members(self):
        """  'getter' of group max members amount """
        return {self.__max_members}

    def set_max_members(self, set_members):
        """ 'setter' of group max members amount """

        if type(set_members) is int:
            self.__max_members = set_members
        else:
            'some titles naming global exception go here'

    def get_title(self):
        """  'getter' of group title """
        return self.__title

    def set_title(self, new_title):
        """ 'setter' of group title """

        # todo some more advanced title check rule and exception
        if type(new_title) is str:
            self.__title = new_title
        else:
            'some titles naming global exception go here'

    def search_member(self, search_parameter):
        """ group members filter by surname, return list with matched members """
        result = []
        for member in self.__members:
            if search_parameter in member:
                result.append(member)

        return result

    def add_member(self, member):
        if member not in self.__members and len(self.__members) < self.__max_members:
            self.__members.append(member)

    def remove_member(self, member):
        if member in self.__members:
            self.__members.remove(member)

    def __str__(self):
        return f'\nGroup "{self.__title}" ' \
               f'include {len(self.__members)} members:\n\t' + '\n\t'.join(map(str, self.__members)) + '\n'


# 'entry point'
if __name__ == '__main__':

    some_std_group = Group()
    some_std_group.set_title('Nice study hub')
    some_std_group.set_max_members(10)

    some_std_group.add_member(Student('Alex', 'Lavrenchuk', 'A'))
    some_std_group.add_member(Student('Guido', 'Rossum', 'A++'))
    some_std_group.add_member(Student('Helga', 'Hansen', 'A'))
    some_std_group.add_member(Student('Peter', 'Pen', 'B'))
    some_std_group.add_member(Student('Vasyl', 'Zaliznyak', 'A'))

    print(f'\nMembers limit of "{some_std_group.get_title()}" is {some_std_group.get_max_members()} members.')

    print(some_std_group)

