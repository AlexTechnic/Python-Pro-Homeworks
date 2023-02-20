"""
2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася
виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати). Подію додавання нового студента до групи
необхідно фіксувати у лог-файлі. """

import logging

# create logger
logger = logging.getLogger('homework_03_members')
logger.setLevel(logging.INFO)

# create file handler and set level to info
ch = logging.FileHandler("homework_03_members.log")
ch.setLevel(level=logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


class GroupLimitError(Exception):
    def __init__(self, max_members, title):
        self.max_members = max_members
        self.title = title

    def __str__(self):
        return f'In group "{self.title}" are already {self.max_members} members.'


class SameMemberError(Exception):
    def __init__(self, member, group_title):
        self.member = member
        self.group_title = group_title

    def __str__(self):
        return f'Member {self.member}, already registered in group "{self.group_title}".'


class Human:
    def __init__(self, name: str = 'Name', surname: str = 'Surname', age: int = 18, born: str = '2006',
                 cellphone: str = 'XXXXXXXXXX', email: str = 'mail@domain.com'):
        if not isinstance(age, int):
            raise TypeError()

    # maybe better if all attributes was 'protected' and using setters and getters methods instead to work with them?
        self.name = name
        self.surname = surname
        self.age = age
        self.born = born
        self.cellphone = cellphone
        self.email = email

    def __str__(self):
        return f'\nName: {self.name}' \
               f'\nsurname: {self.surname}' \
               f'\nBorn: {self.born} ' \
               f'\nCellphone: {self.cellphone}' \
               f'\nEmail: {self.email}'


class Student(Human):

    def __init__(self, name, surname, age, grade):
        super().__init__(name, surname, age)
        self.grade = grade

    def __str__(self):
        return f'{self.name} {self.surname}, age {self.age} (grade {self.grade})'


class Group:
    def __init__(self, title: str = 'Group title', max_members: int = 1):
        self.__title = title
        self.__max_members = max_members
        self.__members = []

    def get_max_members(self):
        """  'getter' of group max members limit """
        return {self.__max_members}

    def set_max_members(self, set_members):
        """ 'setter' of group max members limit """

        if not isinstance(set_members, int):
            raise TypeError()
        if set_members <= 0:
            raise ValueError()

        self.__max_members = set_members

    def get_title(self):
        """  'getter' of group title """
        return self.__title

    def set_title(self, new_title):
        """ 'setter' of group title """

        if not isinstance(new_title, str):
            raise TypeError()

        self.__title = new_title

    def add_member(self, member):
        if member in self.__members:
            raise SameMemberError(member, self.__title)
        if len(self.__members) >= self.__max_members:
            raise GroupLimitError(self.__max_members, self.__title)

        self.__members.append(member)

    def remove_member(self, member):
        if not isinstance(member, Human):
            raise TypeError()
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
    try:

        # creating study group 'Nice study hub' based on 'Group' class
        std_group = Group()
        std_group.set_title('Nice study hub')
        std_group.set_max_members(10)

        # creating students instances based on 'Student' class
        stud_01 = Student('Ivan', 'Melnik', 21, 'A')
        stud_02 = Student('Guido', 'Rossum', 24, 'A+')
        stud_03 = Student('Helga', 'Hansen', 26, 'A')
        stud_04 = Student('Peter', 'Pen', 21, 'B')
        stud_05 = Student('Migel', 'Barbados', 28, 'A')
        stud_06 = Student('Bart', 'Smith', 19, 'B')
        stud_07 = Student('Rick', 'Sanchez', 52, 'A+')
        stud_08 = Student('Georg', 'Smith', 24, 'A')
        stud_09 = Student('Alexander', 'Melnik', 25, 'A')
        stud_10 = Student('Vasyl', 'Zaliznyak', 23, 'A')

        stud_11 = Student('Debora', 'Morgan', 17, 'A')

        # adding students instances to group
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

        # searching in group
        search_query = input(str('Please enter in-group search query: '))
        bs_t = '\n\t'  # adding support of backslash characters to f-string
        print(f"\nUsing 'group.search' method in group '{std_group.get_title()}' "
              f"\nsearching '{search_query}' "
              f"\nfound {len(std_group.search_members(search_query))} matches "
              f"\n\t{bs_t.join(std_group.search_members(search_query))}")

        logger.info('Process finished successfully, logging stopped.')

    except Exception as error:
        print(f'Process terminated by exception, message:\n\t{error}\n')
        logger.info(f'Process terminated by exception, message: <{error}> , logging stopped.\n')
