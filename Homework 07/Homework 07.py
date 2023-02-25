"""
1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на
завершення.

2. Реалізуйте свій аналог генераторної функції range().

3. Напишіть функцію-генератор, яка повертатиме
прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.

4. Напишіть генераторний вираз для
заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини. """


# TASK 1
#  creating geometric progression generator func
def geometric_progression(start_num: int = 1, mul: int = 2, lim: int = 65_535) -> int:
    """
    Generate geometric progression int numbers (previous number * multiplier, than next step)

    Parameters
    ----------
    start_num - first number that geometric progression starts
    mul - multiplier of geometric progression
    lim - limit of progression next step number count that will cause exception
    Generate geometric progression int numbers (previous number * multiplier, than next)
    -------
    """
    mem = start_num
    while mem * mul <= lim:
        yield mem * mul
        mem *= mul
    return


g = geometric_progression()

# printing to output
print('TASK 1:')
user_stop_num = input('Please enter user defined int number that will stop progression generator (enter = skip): ')
if user_stop_num.isnumeric():
    user_stop_num = int(user_stop_num)


def print_g_prog(steps):
    """ making some options for printing output of geometric progression func"""

    for i in range(steps):
        inner_mem = next(g)
        print(inner_mem)
        if inner_mem == user_stop_num:
            g.close()
            print(f'Error: generator output matches user defined stop value: {user_stop_num}')


print(f'\nThere is a geometric progression:')
print_g_prog(10)
print('')


# TASK 2
def range_func(*args):
    """
    Custom range func

    Parameters
    ----------
    args - 'mem' (start/memorized last value), 'step' (+... value), 'stop' (do until 'stop')

    Returns range of values between 'mem' -> 'stop' with step +'step'
    -------
    """

    if not args or len(args) > 3:
        raise TypeError

    mem = args[0] if len(args) >= 2 else 0
    step = args[1] if len(args) >= 2 else args[0]
    stop = args[2] if len(args) == 3 else 1

    if not step:
        raise ValueError

    if mem < 0 and stop > mem:
        return

    if step > 0 and stop < mem:
        return

    while mem < stop:
        yield mem
        mem += step
    return


my_range_start = 2.54
my_range_step = 2.54
my_range_stop = 100

my_range = range_func(my_range_start, my_range_step, my_range_stop)

print('TASK 2:')
print(f"Custom range func. Limits [{my_range_start}:{my_range_stop}], step +{my_range_step}.")
print(f"Example of usage: generation of inches values in 100 cm range:\n")

my_range_index = 0
for i in my_range:
    print(f'{my_range_index + 1}" = {round(i,2)} cm')
    my_range_index += 1
my_range_index = 0

input('\nPress enter to continue: ')


# TASK 3
def prime_gen(calc_lim):
    """
    Func that generates range of cube numbers.

    Parameters
    ----------
    calc_lim - int, upper limit of calculation.

    Returns - range of int prime numbers between 0 and user defined limit.
    -------
    """

    START = 2   # constant first number of prime numbers, always = 2

    while START <= calc_lim:
        prime_numbers_list = [1 for i in range(2, START + 1) if START % i == 0]
        if len(prime_numbers_list) > 1:
            START += 1
            continue
        else:
            yield START
        START += 1
    return


# usage of prime generator func
prime_gen_lim = 100
prime_gen_index = 1

print('\nTASK 3:')
print(f"Generation of prime numbers between 0:{prime_gen_lim} range:\n")
for i in prime_gen(prime_gen_lim):
    print(f"prime num {prime_gen_index}:  {i}")
    prime_gen_index += 1
prime_gen_index = 1

input('\nPress enter to continue: ')


# TASK 4
# expression that generates list of cubes numbers (n**3) from user defined numbers range [start:end]
cubes_start = 2
cubes_end = 10
cubes = (item ** 3 for item in range(cubes_start, cubes_end))
cubes_list = [*cubes]

# printing to output
print('\nTASK 4:')
res_text = f'List of cubes numbers calculating in range [{cubes_start}:{cubes_end}]:\n{cubes_list}'
print(res_text)
