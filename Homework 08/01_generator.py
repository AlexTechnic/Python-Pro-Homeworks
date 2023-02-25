# generator of sequence of numbers
def generator(start: int, stop: int):
    """
    Generator func that yields numbers from user defined numbers sequence.
    Parameters
    ----------
    start - first number of sequence.
    stop - defines qty of numbers in sequence, from 0 to stop [0:stop]

    Returns each next number value from sequence step-by-step.
    -------

    """
    for num in range(start, stop):
        x = user_func(num)
        if stop_generator(x):
            raise ValueError
        yield x
        stop += 1
        if stop > stop:
            break


# user defined expression rule that stops generator
def stop_generator(num):
    """
    Func that checking generator values for match exception pattern by user defined rules.
    Parameters
    ----------
    num - number of sequence that comes from generator func.

    Return - if True - match found, False - not found.
    -------
    """
    if num > 1000 or num < 0:  # MODIFY EXCEPTION RULE HERE
        return True


# user defined function formula applied to generator
def user_func(num: int): return num ** 3


# printing output
gen1 = generator(0, 20)

try:
    for i in gen1:
        print(i)
except ValueError:
    print('Stopped: generator value matches user defined exception rule.')
