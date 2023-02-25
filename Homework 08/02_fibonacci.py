"""
2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація -
https://en.wikipedia.org/wiki/Memoization . Використовуйте отриманий механізм для прискорення функції
рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.
"""

import timeit
# from functools import lru_cache


# 1st simple recursion fibonacci algorithm
def rec_fib(n):
	if n == 1 or n == 2:
		return 1
	return rec_fib(n - 1) + rec_fib(n - 2)


# # 2nd fibonacci recursion algorithm with 'memoization' (using functools lib)
# @lru_cache()
# def rec_fib_lru(n):
#     if n == 1 or n == 2:
#         return 1
#     return rec_fib_lru(n - 1) + rec_fib_lru(n - 2)


# 3rd manual fibonacci recursion algorithm with 'memoization'
def rec_fib_mem_():
	temp = [0, 1]

	def get_next(n):
		if n < len(temp):
			return temp[n]
		curr, next = temp[-2], temp[-1]
		indx = len(temp)
		while indx <= n:
			curr, next = next, curr + next
			temp.append(next)
			indx += 1
		return next

	return get_next


rec_fib_mem = rec_fib_mem_()

# enter here user defined fibonacci number to calculate
calc_num = 15

# enter here how many cycles need to do to calculate performance
run_cycles = 15

# assign algorithms funcs to short names
func_1 = rec_fib(calc_num)  # simple
# func_2 = rec_fib_lru(calc_num)  # with lib
func_3 = rec_fib_mem(calc_num)  # with memo

# preparation to calculate performance of 1st algorythm
func_1_t = f"""
def rec_fib(n):
    if n == 1 or n == 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

func_1 = rec_fib({calc_num})
"""


# sub-func using in cycle of performance calculation
def time_calc1(): return timeit.timeit(func_1_t, number=1000)


# cycle to calculate min and avg time of execution 3rd algorythm
res_time_calc1 = []
for n in range(0, run_cycles):
	sub_res = time_calc1()
	res_time_calc1.append(sub_res)

res_min_1 = min(res_time_calc1)
res_avg_1 = sum(res_time_calc1) / len(res_time_calc1)

# preparation to calculate performance of 3rd algorythm (memoization)
func_3_t = f"""
def rec_fib_mem_():
    temp = [0, 1]
    def get_next(n):
        if n < len(temp):
            return temp[n]
        curr, next = temp[-2], temp[-1]
        indx = len(temp)
        while indx <= n:
            curr, next = next, curr + next
            temp.append(next)
            indx += 1
        return next
    return get_next

rec_fib_mem = rec_fib_mem_()

func_3 = rec_fib_mem({calc_num})
"""


# sub-func using in cycle of performance calculation
def time_calc3(): return timeit.timeit(func_3_t, number=1000)


# cycle to calculate min and avg time of execution 3rd algorythm (memoization)
res_time_calc3 = []
for n in range(0, run_cycles):
	sub_res = time_calc3()
	res_time_calc3.append(sub_res)

res_min_3 = min(res_time_calc3)
res_avg_3 = sum(res_time_calc3) / len(res_time_calc3)

# printing to output
print(f'\nTime for calculate fibonacci num (№{calc_num} = {rec_fib(calc_num)}) using simple recursion:'
      f'\n\tmin: {res_min_1:.3f} ms, avg: {res_avg_1:.3f} ms ({run_cycles} x times re-run)')

print(f'\nTime for calculate fibonacci num (№{calc_num} = {rec_fib_mem(calc_num)}) with memoization:'
      f'\n\tmin: {res_min_3:.3f} ms, avg: {res_avg_3:.3f} ms ({run_cycles} x times re-run)')

print(f'\nAverage boost of using memoization for calculate fibonacci number №{calc_num} '
      f'= +{(res_avg_1 / res_avg_3) * 100:.2f}%')
