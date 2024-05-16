# Работа с переменными
# 1. Переменной var_int присвойте значение 10,
# var_float - значение 8.4, var_str - "No".

var_int = 10
var_float = 8.4
var_str = 'No'

# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.

big_int = var_int * 3.5

# 3. Измените значение, хранимое в переменной var_float,
# уменьшив его на единицу, результат свяжите с той же переменной.

var_float = var_float - 1

# 4. Разделите var_int на var_float, а затем big_int на var_float.
# Результат данных выражений не привязывайте ни к каким переменным.

# 5. Измените значение переменной var_str на "NoNoYesYesYes".
# При формировании нового значения используйте операции конкатенации (+)
# и повторения строки (*).

# 6. Выведите значения всех переменных.

print(' big_int =', big_int, '\n', 'var_float =', var_float, '\n',
      'var_int / var_float =', var_int / var_float, '\n',
      'big_int / var_float =', big_int / var_float, '\n',
      'var_str =', var_str * 2 + 'Yes' * 3)

# Строки
# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний,
# третий с начала и третий с конца.
# Измерьте длину вашей строки.

a = '123qwerty'
print(a[0], a[-1], a[2], a[-3])
print('длина строки = ', len(a))

# 2. Присвойте произвольную строку длиной 10-15 символов переменной
# и извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем
# переверните строку

b = '123qwertyasdfgh'
index_seredina = (len(b)//2)

print('первые 8 символов =', b[0:8], '\n',
      'четыре символа из центра строки = ',
      b[(index_seredina-2):(index_seredina+2)], '\n',
      'символы с индексами кратные трём =', b[::3], '\n',
      'перевёрнутая строка:', b[::-1])

# 3. Есть строка: “my name is name”.
# Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

my_name = 'my name is name'
name = 'Kristina'
my_name_1 = my_name.split()
print(my_name_1)
del my_name_1[-1]
print(my_name_1)
my_name_1.append(name)
print(my_name_1)
my_name_2 = ' '.join(my_name_1)
print(my_name_2)

# 4. Есть строка: test_tring = "Hello world!", необходимо:
# напечатать на каком месте находится буква w
# кол-во букв l
# проверить начинается ли строка с подстроки: “Hello”
# проверить заканчивается ли строка подстрокой: “qwe”

test_tring = 'Hello world!'
print('Индекс буквы W:', test_tring.index('w'), '\n',
      'Количество букв l: ', test_tring.count('l'))

if test_tring.index('Hello') == 0:
    print('Строка начинается с подстроки "Hello"')
else:
    print('pass')
if test_tring.endswith('qwe') == 1:
    print('Строка заканчивается подстрокой "qwe"')
else:
    print('Строка НЕ заканчивается подстрокой "qwe"')

# списки
# 1. Создайте два любых списка и свяжите их с переменными.

numbers = [2, 4, 6, 8, 10]      # 1
words = ['hello', 'welcome', 'salute', 'hi']

# 2. Извлеките из первого списка второй элемент.

print(numbers[1])

# 3. Измените во втором списке последний элемент.
# Выведите список на экран.

words[-1] = 'salutation'
print(words)

# 4. Соедините оба списка в один, присвоив результат новой переменной.
# Выведите получившийся список на экран.

unification = numbers + words
print(unification)

# 5. "Снимите" срез из соединенного списка так,
# чтобы туда попали некоторые части обоих первых списков.
# Срез свяжите с очередной новой переменной. Выведите значение этой переменной.

unification_1 = unification[0:9:2]
print(unification_1)

# 6. Добавьте в список два новых элемента и снова выведите его.

unification.append('1')
unification.append('hey')
print(unification)

# 7. Даны списки: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов,
# общих для этих двух списков.
# !не использовать циклы

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a).intersection(b)
print(c)

# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
# оставить в нем только уникальные значения. !не использовать циклы

nums = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(nums)))

# Логические операции
# 1. Присвойте двум переменным любые числовые значения.

variable_first = 178
variable_second = 26

# 2. Составьте четыре сложных логических выражения с помощью оператора and,
# два из которых должны давать истину, а два других - ложь.

print(variable_second > variable_first and variable_first != variable_second)
print(variable_first != variable_second and variable_first < variable_second)
print(variable_first != variable_second and variable_first >= variable_second)
print(variable_second < variable_first and variable_first != variable_second)

# 3. Аналогично выполните п.2, но уже используя оператор or.

print(variable_second > variable_second or variable_first == variable_second)
print(variable_first == variable_second or variable_first < variable_second)
print(variable_first != variable_second or variable_first >= variable_second)
print(variable_second < variable_first or variable_first != variable_second)

# 4. Попробуйте использовать в сложных логических
# выражениях работу с переменными строкового типа.

banana = 'banana'
apple = 'apple'

# and

print(banana > apple and banana != apple)
print(banana != apple and banana < apple)
print(banana != apple and banana >= apple)
print(banana < apple and banana != apple)

# or

print(banana <= apple or banana == apple)
print(banana == apple or banana < apple)
print(banana != apple or banana >= apple)
print(banana < apple or banana != apple)

# Словари
# 1. Создайте словарь, связав его с переменной school, и наполните его данными,
#  которые бы отражали количество учащихся в десяти разных классах
#  (например, 1а, 1б, 2б, 6а, 7в и т.д.)

school = {'1a': 20, '1b': 25, '1c': 18, '2a': 25, '2b': 15, '2c': 21,
          '3a': 20, '3b': 25, '3c': 18, '4a': 25, '4b': 15, '4c': 21,
          '5a': 20, '5b': 25, '5c': 18, '6a': 25, '6b': 15, '6c': 21,
          '7a': 20, '7b': 25, '7c': 18, '8a': 25, '8b': 15, '8c': 21,
          '9a': 25, '9b': 15, '9c': 21, '10a': 20, '11a': 25, '11b': 18}

print(school)

# 2. Узнайте, сколько человек в каком-нибудь классе

print(school.get('1a'))

# 3. 1) В трёх классах изменилось колличество учащихся

school['1a'] = 22
school['1c'] = 16
school['7a'] = 21

school['1d'] = 15
school['10b'] = 10  # 2) В школе появилось два новых класса

del school['11b']   # 3) В школе расформировали один из классов

print(school)    # 4. Содержимое словаря

# Преобразование типов
# 1. Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" =>
# => ["I", "love", "arrays", "they", "are", "my", "favorite"]

converting = "Robin Singh"
change = "I love arrays they are my favorite"
print(converting.split())
print(change.split())

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
print('Привет, ', ' '.join(name), '! Добро пожаловать в', city, country)

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

change = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(change))

# 4. Создайте список из 10 элементов,
# вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

change = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
change[2] = 'variables'
del change[6]
print(change)

# 5. Есть 2 словаря a = {'a': 1, 'b': 2, 'c': 3}, b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам,
# а значения ключей поместить в список, если у одного словаря есть ключ "а",
# а у другого нет, то поставить значение None на соответствующую позицию
# (1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None],
# 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

together_keys = set(a.keys()).union(set(b.keys()))
ab = {
    key: [a.get(key, None), b.get(key, None)]
    for key in together_keys
}

print(ab)

# Условия
# 1. Дано целое число.
# Если оно является положительным, то прибавить к нему 1;
# в противном случае не изменять его.
# Вывести полученное число

a = int(input('Введите любое целое число '))
if a >= 0:
    print(a + 1)
else:
    print(a)

# 2. Даны три целых числа.
# Найти количество положительных чисел в исходном наборе.

a, b, c = (int(input('Введите первое целое число ')),
           int(input('Введите второе целое число ')),
           int(input('Введите третье целое число ')))

print((a > 0) + (b > 0) + (c > 0))

# 3. Дан номер года (положительное целое число).
# Определить количество дней в этом году, учитывая,
# что обычный год насчитывает 365 дней, а високосный - 366 дней.
# Високосным считается год, делящийся на 4,
# за исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными,
# а 1200 и 2000 являются).

year = int(input('Введите год '))
if year > 0 and year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print(365)
elif year < 0:
    print(ValueError)
else:
    print(366)

# 4. Дано целое число в диапазоне 1-7. Вывести строку - название дня недели,
# соответствующее данному числу (1 - "понедельник", 2 - "вторник" и т.д.)

week = int(input('Введите целое число от 1 до 7: '))
if 7 >= week >= 1:
    if week == 1:
        print('Понедельник')
    if week == 2:
        print('Вторник')
    if week == 3:
        print('Среда')
    if week == 4:
        print('Четверг')
    if week == 5:
        print('Пятница')
    if week == 6:
        print('Суббота')
    if week == 7:
        print('Воскресенье')
else:
    print(ValueError)

# 5. Единицы массы пронумерованы следующим образом:
# 1 - килограмм, 2 - миллиграмм, 3 - грамм, 4 - тонна, 5 - центнер.
# Дан номер единицы массы (целое число в диапазоне 1-5)
# и масса тела в этих единицах (вещественное число).
# Найти массу тела в килограммах.

mass_input = int(input('Введите число от 1 до 5: '))
weight = int(input('Введите массу: '))
if mass_input == 1:
    print(weight, 'килограмм')
elif mass_input == 2:
    weight = weight * (10**6)
    print(weight, 'килограмм')
elif mass_input == 3:
    weight = weight * (10**3)
    print(weight, 'килограмм')
elif mass_input == 4:
    weight = weight * (10**-3)
    print(weight, 'килограмм')
elif mass_input == 5:
    weight = weight * (10**-2)
    print(weight, 'килограмм')
else:
    print('Вы ввели неправильное число')

# Цикл for
# 1. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.

a = int(input('Введите целое число: '))
b = int(input('Введите целое число, больше предыдущего: '))
smm = 0
for i in range(a, b + 1):
    smm += i
print('Сумма всех целых чисел = ', smm)

# 2. Найти сумму всех натуральных чисел от A и B

smm_nat = 0
for j in range(a, b + 1):
    if j > 0:
        smm_nat += j
print('Сумма всех натуральных чисел = ', smm_nat)

# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.

q, w, e, r, t, y, u, k, o, p = (int(input('Введите первое число: ')),
                                int(input('Введите 2-е число: ')),
                                int(input('Введите 3-е число: ')),
                                int(input('Введите 4-е число: ')),
                                int(input('Введите 5-е число: ')),
                                int(input('Введите 6-е число: ')),
                                int(input('Введите 7-е число: ')),
                                int(input('Введите 8-е число: ')),
                                int(input('Введите 9-е число: ')),
                                int(input('Введите 10-е число: ')))

summiryem = 0
proizv = 1
kolich = 0
for i in q, w, e, r, t, y, u, k, o, p:
    if i > 0:
        proizv *= i
    if i < 0:
        summiryem += i
        kolich += 1
print('Сумма отрицательных = ', summiryem,
      'Количество отрицательных = ', kolich)
print('Произведение положительных = ', proizv)

# 4. Дан словарь пловцов с их результатами.
# Напечатать лучший результат заплыва среди 6 участников.

dict_1 = {'Бекиш Александр': 21.07, 'Будник Алексей': 20.34,
          'Гребень Анастасия': 22.12, 'Давидович Татьяна': 30,
          'Дешук Дмитрий': 24.01, 'Казак Анна': 28.17}
vin = 1
for i in dict_1:
    if i > vin:
        vin = i
print(vin)

# 5. Есть массив чисел.
# Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1]
# Напишите программу, которая будет выводить уникальное число

d = [1, 5, 2, 9, 2, 9, 1]
a = []
for i in d:
    if d.count(i) == 1:
        a.append(i)
print(a)

# Цикл while
# 1. Дано число N. Найти произведение чисел от 0 до N.

n = int(input('Введите целое число: '))
num = 1
while n != 0:
    num *= n
    n -= 1

print('Произведение чисел равно ', num)

# 2. Поле засеяли цветами двух сортов площади S1 И S2.
# Каждый год площадь цветов первого сорта увеличивается вдвое,
# а площадь второго сорта увеличивается втрое.
# Через сколько лет площадь первых сортов будет составлять
# меньше 10% от площади вторых сортов

S1 = int(input('Введите целое число: '))
S2 = int(input('Введите целое число: '))
years = 0
while S1 > (S2 / 10):
    years += 1
    S1 *= 2
    S2 *= 3
print('Через ', years, 'лет/года')

# 3. Дано целое число N (>0).
# Используя операции деления нацело и взятия остатка от деления,
# найти количество и сумму его цифр.

number = int(input('Введите целое число: '))
s = []
while number != 0:
    s.append(number % 10)
    number = number // 10
print('Количество цифр равно: ', len(s), 'Сумма цифр числа равно: ', sum(s))

# 4. Деду М лет, а внуку N лет.
# Через сколько лет дед станет вдвое старше внука.
# И сколько при этом лет будет деду и внуку.

m = 50
n = 5
year = 0
while m / n != 2:
    year += 1
    n += 1
    m += 1

print('Через ', year, 'лет дед станет вдвое старше внука.', '\n',
      'Возраст деда: ', m, 'Возраст внука: ', n)
