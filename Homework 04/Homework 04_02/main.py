"""
2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів, викликалася
виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати). Подію додавання нового студента до групи
необхідно фіксувати у лог-файлі. """

import logging
import student
import group

# create logger
logger = logging.getLogger("Homework 04_02")
logger.setLevel(logging.INFO)

# create file handler and set level to info
ch = logging.FileHandler("members.log")
ch.setLevel(level=logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


# 'entry point'
if __name__ == '__main__':
    try:

        # creating study group 'Nice study hub' based on 'Group' class
        std_group = group.Group()
        std_group.set_title('Nice study hub')
        std_group.set_max_members(10)

        # creating students instances based on 'Student' class
        stud_01 = student.Student('Ivan', 'Melnik', 21, 'A')
        stud_02 = student.Student('Guido', 'Rossum', 24, 'A+')
        stud_03 = student.Student('Helga', 'Hansen', 26, 'A')
        stud_04 = student.Student('Peter', 'Pen', 21, 'B')
        stud_05 = student.Student('Migel', 'Barbados', 28, 'A')
        stud_06 = student.Student('Bart', 'Smith', 19, 'B')
        stud_07 = student.Student('Rick', 'Sanchez', 52, 'A+')
        stud_08 = student.Student('Georg', 'Smith', 24, 'A')
        stud_09 = student.Student('Alexander', 'Melnik', 25, 'A')
        stud_10 = student.Student('Vasyl', 'Zaliznyak', 23, 'A')

        stud_11 = student.Student('Debora', 'Morgan', 17, 'A')

        # func to add some students instances to group with printing + logging
        def std_group_add_member(name):
            std_group.add_member(name)
            print(f'Added {name} to the "{std_group.get_title()}"')
            logger.info(f'Added {name} to the "{std_group.get_title()}"')

        # adding students to group
        std_group_add_member(stud_01)
        std_group_add_member(stud_02)
        std_group_add_member(stud_03)
        std_group_add_member(stud_04)
        std_group_add_member(stud_05)
        std_group_add_member(stud_06)
        std_group_add_member(stud_07)
        std_group_add_member(stud_08)
        std_group_add_member(stud_09)
        std_group_add_member(stud_10)
        # std_group_add_member(stud_11)

        # print(f'\nMembers limit of "{std_group.get_title()}" is {str(std_group.get_max_members())[1:-1]} members')
        # print(std_group)

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