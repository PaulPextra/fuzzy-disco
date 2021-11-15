import os
os.system('cls')

class Person:

    num_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_people() # Initializing the class method
        
    @classmethod
    def number_of_people(cls):
        return cls.num_of_people

    @classmethod
    def add_people(cls):
        cls.num_of_people += 1

    @staticmethod
    def add_5(x):
        return x + 5

p1 = Person('Paul')
p2 = Person('John')
p3 = Person('Jim')

print(Person.number_of_people())

print(Person.add_5(6))

def func(fruit = 'Mango'):
    return f'My favorite fruit is {fruit}'

print(func())


# Concept of Polymorphism
'''
# Polymorphism in Python

Polymorphism in OOP is the ability of an object to take many forms. In simple words, polymorphism allows us to perform the same action in many different ways.

Polymorphism is taken from the Greek words Poly (many) and morphism (forms). Polymorphism defines the ability to take different forms.
'''
class Circle:
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)

# function
def area(shape):
    # call action
    shape.calculate_area()

# create object
cir = Circle(5)
rect = Rectangle(10, 5)

# call common function
area(cir)
area(rect)