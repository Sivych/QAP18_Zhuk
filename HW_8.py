# 1. Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы


def factorial(num):
    fct = 1
    for i in range(1, num+1):
        fct *= i
    return fct


def factorial_generator(num):
    fct = 1
    for i in range(1, num+1):
        fct *= i
        yield fct


def factorial_recursive(num):
    if num == 0:
        return 1
    return num * factorial_recursive(num-1)


import timeit

# код, время выполнения которого нужно измерить
code_to_test = """
def factorial(num):
    fct = 1
    for i in range(1, num+1):
        fct *= i
    return fct
    
factorial(5)
"""

# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=1)
print('Elapsed time: ', elapsed_time)

code_to_test_generator = """
def factorial_generator(num):
    fct = 1
    for i in range(1, num+1):
        fct *= i
        yield fct

factorial_generator(5)
"""

elapsed_time_generator = timeit.timeit(code_to_test_generator, number=1)
print('Elapsed time generator: ', elapsed_time_generator)

code_to_test_recursive = """
def factorial_recursive(num):
    if num == 0:
        return 1
    return num * factorial_recursive(num-1)

factorial_recursive(5)
"""

elapsed_time_recursive = timeit.timeit(code_to_test_recursive, number=1)
print('Elapsed time recursive: ', elapsed_time_recursive)

# 2. Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:

# @typed(type=’str’)
# def add_two_symbols(a, b):
#     return a + b
#
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> 55
# add_two_symbols('a', 'b') -> 'ab’

# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#     return a + b + с
#
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4)
# -> 0.7000000000000001


def typed(type):
    def my_shiny_new_decorator(function_to_decorate):
        def the_wrapper_around_the_original_function(*args):
            new_args = []
            for i in args:
                if type == 'str':
                    new_args.append(str(i))
                elif type == 'int':
                    new_args.append(float(i))
                else:
                    new_args.append(i)
    # Вернём эти функции
            return function_to_decorate(*new_args)
        return the_wrapper_around_the_original_function
    return my_shiny_new_decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols('3', 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))

