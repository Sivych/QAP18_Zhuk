# 1. Привести к целому типу

a = 1.6
b = 2.99
print(int(a), int(b))

# 2. Заменить символ # на /

str = 'www.my_site.com#about'
x = str.replace('#', '/')
print(x)

# 3. Добавить 'ing' к слову 'stroka'

str1 = 'stroka'
str2 = str1 + 'ing'
print(str2)

# 4. В строке 'Ivanov Ivan' поменяйте местами слова => 'Ivan Ivanov'

str3 = 'Ivanov Ivan'
s = str3.find(' ')
str4 = int(s)
new_str = str3[(s+1)::] + ' ' + str3[0:s]
print(new_str)

# 5. Напишите программу которая удаляет пробел вначале и в конце строки

str5 = ' stroka '
new_str1 = str5.strip()
new_str2 = new_str1.rstrip()
print(new_str2)

# 6. Создайте словарь, связав его с переменной school, и наполните его данными, \
#   которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.)

school = { '1a': 20, '1b': 25, '1c': 18, '2a': 25, '2b': 15, '2c': 21, '3a': 20, '3b': 25, '3c': 18,\
         '4a': 25, '4b': 15, '4c': 21, '5a': 20, '5b': 25, '5c': 18, '6a': 25, '6b': 15, '6c': 21,\
         '7a': 20, '7b': 25, '7c': 18, '8a': 25, '8b': 15, '8c': 21, '9a': 25, '9b': 15, '9c': 21,\
         '10a': 20, '11a': 25, '11b': 18 }

print(school)

# 7. Создайть список и извлечь из него второй элемент

spisok = [0, 5, 5556, 584, 956, 78]
print(spisok[1])

# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment)

strochka1 = 'квадрат'
strochka2 = 'квадратный'
if strochka2.find('квадрат') == 0:
    print('yes')
else:
    print('no')

# 9. Вывести нужные символы #y #nesgt

x = 'My name is Agent Smith'
print(x[1])
print(x[3:16:3])

# 10. Напишите программу, которая будет выводить уникальное число

d = [1, 5, 2, 9, 2, 9, 1]
a = []
for i in d:
    if d.count(i) == 1: #количество вхождений
        a.append(i)
print(a)

def operate(*args, operation):
    if operation == 'sum':
        return sum(args)
    print(operate(1, 2, 3, 4, operation='sum'))

print(operate(1, 2, 3, 4, operation='sum'))         # Вывод: 10
print(operate(1, 2, 3, 4, operation='multiply'))    # Вывод: 24
print(operate(1, 2, 3, 4, operation='subtract'))    # Вывод: Unsupported operation

#name = 'Egor'
#age = '68'
#str = f"hello, {name}, {age}"
#print(str)
#def open_files(*args, mode):


#open_files('file1.txt', 'file2.txt', mode='r')
# 'r' - чтение
# 'w' - запись
 #   if mode == 'r':
 #       return 'Открыты для чтения'
#print("file1.txt, 'file2.txt', Открыты для чтения")


#def open_files(*args, mode):
  #  str = ''
 #   for i in args:
  #      str+=i
  #  if mode == "r":
  #      print(f" {str}, Открыто для чтения")
  #  elif mode == "w":
  #      print(f" {str}, Открыто для записи")
  #  else:
  #      print(':(((')


#def print_users(**kwargs, args):


#print_users(
#    John=dict(age=30, city='New York'),
#    Alice=dict(age=25, city='San Francisco')
#)
#str = ''
#    for i in args:
 #       print(f" {age}")
# Вывод:
# User: John
# age: 30
# city: New York
#
# User: Alice
# age: 25
# city: San Francisco
# str = f"hello, {name}, {age}"




#sqr(2)  == 4
#cube(2) == 8

def pow(num1):
    def inner(num2):
        return num2 ** num1
    return inner


sqr = pow(2)
cube = pow(3)


print(sqr(2))
print(cube(2))

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

together_keys = set(a.keys()).union(set(b.keys()))
c = {
    key: [a.get(key, None), b.get(key, None)]
    for key in together_keys
}

print(c)