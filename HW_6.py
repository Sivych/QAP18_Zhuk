# 1. Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного файла.
# Если чисел меньше 3 выводить ошибку
# import os


def read_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        elements = file.read().split()

        if len(elements) < 3:
            print('Error')
        else:
            print(elements[0], elements[1], elements[-2], elements[-1])


read_file("HW_6_1.txt")

# 2. Дан файл целых чисел.
# Создать два новых файла, первый из которых содержит четные числа
# из исходного файла, а второй — нечетные (в том же порядке).
# Если четные или нечетные числа в исходном файле отсутствуют,
# то соответствующий результирующий файл оставить пустым.


def write_file(file):
    file = open(file, 'r', encoding='utf-8')
    readable = file.read().split()
    even_file = open("even_numbers.txt", 'w', encoding='utf-8')
    odd_file = open("odd_numbers.txt", 'w', encoding='utf-8')

    for i in readable:
        if int(i) % 2 == 0:
            even_file.write(i + ' ')
        else:
            odd_file.write(i + ' ')

    file.close()
    even_file.close()
    odd_file.close()


write_file("HW_6_1.txt")

# 3. Дан файл вещественных чисел.
# Заменить в нем все элементы на их квадраты.


def squares_of_num(file):
    file = open("float_numbers.txt", 'r', encoding='utf-8')
    float_num = file.read().split()
    n = []

    for i in float_num:
        n.append(float(i) ** 2)

    file.close()
    file = open("float_numbers.txt", 'w', encoding='utf-8')

    for i in n:
        file.write(str(i) + ' ')

    file.close()


squares_of_num("float_numbers.txt")

# 4. Даны два файла произвольного типа.
# Поменять местами их содержимое. Файлы должны быть бинарного типа.
# Все делать с помощью функций.
