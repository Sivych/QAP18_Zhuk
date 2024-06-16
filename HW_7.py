# 1. Создать lambda функцию,
# которая принимает на вход имя и выводит его в формате “Hello, {name}”

func = lambda name: f'Hello, {name}'


print(func('Кристина'))

# 2. Создать lambda функцию,
# которая принимает на вход список имен и
# выводит их в формате “Hello, {name}” в другой список

func_1 = lambda *name: list(map(lambda n: f'Hello, {n}', name))


print(func_1('Кристина', 'Катя', 'Алина'))

# -------------------------------------------------
# 1. Напишите генератор, который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# и возвращает новый список только с положительными числами


def create_generator():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for i in numbers:
        if i > 0:
            yield i


my_generator = create_generator()
print(next(my_generator))
for i in my_generator:
    print(i)


# 2. Необходимо составить список чисел,
# которые указывают на длину слов в строке:
# sentence = "thequick brown fox jumps over the lazy dog",
# но только если слово не "the" с обработкой исключений


class MyException(Exception):
    pass


sentence = 'thequick brown fox jumps over the lazy dog'
words_length = []
try:
    for word in sentence.split(' '):
        if word == 'the':
            raise MyException
        else:
            words_length.append(len(word))

except MyException:
    print('Exception')

print(words_length)
