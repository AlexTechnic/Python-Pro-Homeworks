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
        return f'{self.name} {self.surname} (grade {self.grade})'


class Group:
    def __init__(self):
        self.__title = 'Group title'
        self.__max_members = int()
        self.__members = []

    def get_max_members(self):
        """  'getter' of group max members limit """
        return {self.__max_members}

    def set_max_members(self, set_members):
        """ 'setter' of group max members limit """

        if type(set_members) is int:
            self.__max_members = set_members
        else:
            'some titles naming global exception go here'

    def get_title(self):
        """  'getter' of group title """
        return self.__title

    def set_title(self, new_title):
        """ 'setter' of group title """

        # todo some more advanced check rule and exception
        if type(new_title) is str:
            self.__title = new_title
        else:
            'some titles naming global exception go here'

    def add_member(self, member):
        if member not in self.__members and len(self.__members) < self.__max_members:
            self.__members.append(member)

    def remove_member(self, member):
        if member in self.__members:
            self.__members.remove(member)

    def search_members(self, search_item):
        """ in-group search method, return list with search query matches """

        result = []

        for member in self.__members:
            if search_item in str(member):
                result.append(str(member))
        return result

    def __str__(self):
        return f'\nGroup "{self.__title}" ' \
               f'include {len(self.__members)}/{self.__max_members} members\n\t' \
               + '\n\t'.join(map(str, self.__members)) + '\n'


# 'entry point'
if __name__ == '__main__':

    # creating study group based on Group class
    std_group = Group()
    std_group.set_title('Nice study hub')
    std_group.set_max_members(10)

    # creating students instances based on Student class
    stud_01 = Student('Ivan', 'Melnik', 'A')
    stud_02 = Student('Guido', 'Rossum', 'A+')
    stud_03 = Student('Helga', 'Hansen', 'A')
    stud_04 = Student('Peter', 'Pen', 'B')
    stud_05 = Student('Migel', 'Barbados', 'A')
    stud_06 = Student('Bart', 'Smith', 'B')
    stud_07 = Student('Rick', 'Sanchez', 'A+')
    stud_08 = Student('Georg', 'Smith', 'A')
    stud_09 = Student('Alexander', 'Melnik', 'A')
    stud_10 = Student('Vasyl', 'Zaliznyak', 'A')

    stud_11 = Student('Debora', 'Morgan', 'A')

    # adding students instances to study group
    std_group.add_member(stud_01)
    std_group.add_member(stud_02)
    std_group.add_member(stud_03)
    std_group.add_member(stud_04)
    std_group.add_member(stud_05)
    std_group.add_member(stud_06)
    std_group.add_member(stud_07)
    std_group.add_member(stud_08)
    std_group.add_member(stud_09)
    std_group.add_member(stud_10)

    std_group.add_member(stud_11)

    print(f'\nMembers limit of "{std_group.get_title()}" is {str(std_group.get_max_members())[1:-1]} members')
    print(std_group)

    # search in group
    search_query = input(str('Please enter in-group search query: '))
    bs_t = '\n\t'  # adding support of backslash characters to f-string
    print(f"\nUsing 'group.search' method in group '{std_group.get_title()}' "
          f"\nsearching '{search_query}' "
          f"\nfound {len(std_group.search_members(search_query))} matches "
          f"\n\t{bs_t.join(std_group.search_members(search_query))}")
