import numpy as np

class Grandmother:

    def __init__(self, name = None, age = None):

        if name is not None and age is not None:
            self.name = name
            self.age = age
        else:
            self.name = "Default"
            self.age = 80

    def printSelf(self):
        print(self.name)
        print(self.age)


a = Grandmother("Name1", 40)

a.printSelf()

numbers = [1,2,3,4,5]
odd = filter(lambda x: x%2 == 1, numbers)

print(type(list(odd)))

print(sum(numbers))

