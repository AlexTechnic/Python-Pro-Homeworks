"""
3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів
отриманого списку.
"""

from random import sample as random_list
from inspect import getsource as code_str


def new_list(n, func):
    """ Func that return new modified list """
    res = []
    for number in n:
        sub_res = (func(number))
        res.append(sub_res)
    return res


# sum func
def new_list_sum(n, func):
    """ Func that calculates sum value of modified elements in list """

    return sum(func(number) for number in n)


# generating list of random int numbers, args: min number, max number, list elements qty
user_list = random_list(range(-10, 10), 10)


# user defined custom formula func, MODIFY USER FUNC HERE:
def user_func(x):
    """ User defined func for list elements (x = list element) """

    return (x**3) - (x**2)


# using imported from 'inspect' func to get 'source code' of user func
user_code = code_str(user_func)

# calculating new list with user func
list_after_str = new_list(user_list, user_func)

# calculating both lists sums before and after formula
sum_before_str = sum(user_list)
sum_after_str = new_list_sum(user_list, user_func)

# printing to output
print(f'\nCalculating elements sum of list before and after apply custom user func to each list element\n')
print(f'List (generated): {user_list}')
print(f'Sum of list elements: {sum_before_str}\n')
print(f'\tapplied for each element func:{user_code.split("return",1)[1]}\t(x = list element)\n')
print(f'New list:{list_after_str}')
print(f'Sum of new list elements (may be float): {sum_after_str}')