# class Magician:
#
#     def __init__(self, name, health, damage, level):
#         self.name: str = name
#         self.health: int = health
#         self.damage: int = damage
#         self.level: int = level
#
#     def healing(self, amount):
#         self.health += amount
#
# fire_magician = Magician('Fire', 17, 5, 5)
# fire_magician.healing(3)
# print(fire_magician.health)
#
#
# class Human:
#
#     def __init__(self, name, date_of_birth, city, gender):
#         self.name: str = name
#         self.date_of_birth: int = date_of_birth
#         self.city: str = city
#         self.gender: str = gender
#
#
# first = Human('Kristina', 26.02, 'Borisov', 'W')
#
# print(first.Human)



class w:
    def __init__(self, continent, individuality):
        self.continent: str = continent
        self.individuality: str = individuality

    def info(self):
        print(self.continent, self.individuality)

class race(w):