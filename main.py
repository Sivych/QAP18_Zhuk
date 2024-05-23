
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

