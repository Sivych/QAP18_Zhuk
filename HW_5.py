# 1. Напишите функцию is_year_leap,
# которая принимает число (год) и возвращает true,
# если год високосный false если нет.


def is_year_leap():
    year = int(input('Введите год '))
    if year > 0 and year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print(False)
    elif year < 0:
        print(ValueError)
    else:
        print(True)


is_year_leap()

# 2. Напишите функцию generate_natural_cubes(n),
# которая принимает число n и возвращает список,
# состоящий из кубов первых n натуральных чисел.
# То есть [1**3, 2**3, 3**3, ..., n**3].
# Обязательно использование генераторов списков.


def generate_natural_cubes():
    n = int(input('Введите целое число'))
    spisok = [i**3 for i in range(1, n+1)]
    print(spisok)


generate_natural_cubes()

# 3. Напишите функцию generate_squares,
# которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9]


def generate_squares(*nums):
    p = []
    for i in nums:
        p.append(i**2)
    print('pow: ', p)


generate_squares(1, 2, 3)
generate_squares(2, 4)

# 4. Напишите функцию get_longest_word,
# которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.


def get_longest_word(string):
    return max(string.split(), key=len)


print(get_longest_word('The longest word in this sentence is - '))




