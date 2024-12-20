# week = {
#     'monday': -1,
#     'tuesday': -5,
#     'wednesday': 3,
#     'thursday': 5,
#     'friday': 9,
#     'saturday': 4,
#     'sunday': 11
# }
# while True:
#     user = input('enter a day: ')
#     if user in week:
#         print(f'{week.get(user)} градусов')
#     else:
#         print('вы неправильно ввели. попробуйте снова.')

class Animal:
    def __init__(self, name,age,energy):
        self.name = name
        self.age = age
        self.__energy = energy

    def speak(self):
       pass
    def __str__(self):
        pass

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = value

    def run(self):
        if self.__energy > 0:
            self.__energy -= 1
            print(f'{self.name} has ran and now has {self.__energy} energy.')
        else:
            print(f'{self.name} has ran and now has no energy.')


class Dog(Animal):
    def __init__(self, name,age,energy):
        super().__init__(name,age,energy)

    def speak(self):
        return 'bark bark'

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Energy: {self.energy}'
class Cat(Animal):
    def __init__(self, name,age,energy):
        super().__init__(name,age, energy)

    def speak(self):
        return 'meow meow'
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Energy: {self.energy}'

cat1 = Cat('Mars', 3, 100)
print(cat1)
print(cat1.speak())
print(cat1.run())
print(cat1.run())




