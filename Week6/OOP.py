import os
os.system("cls")

# Object Oriented Programming
# Convention - pascal case

# Example:
class car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_price(self):
        return self.price

    def get_model(self):
        return self.model

c = car("Toyota", 2000000)
print(c.get_price())
print(c.get_model())

# Class Method
class door:
    width = 4
    @classmethod
    def get_width(cls):
        return cls.width

    @classmethod
    def set_width(cls, value):
        cls.width = value
    
d1 = door()
print(d1.get_width())

class cruise:
    @staticmethod
    def info():
        print("This is a function for cruise and vibes.")
        
cru_vibe = cruise()
print(cru_vibe.info())



class DjangoStudent():
    def __init__(self, name, laptop):
        self.name = name
        self.computer = laptop

mystudent =DjangoStudent("Paul", "HP Envy")
print(mystudent.name)
print(mystudent.computer)

# Example:
class BankApp():
    def __init__(self, name, balance):
        if not isinstance(balance,(int, float)):
            raise TypeError(f'Expected int or float but got {type(balance)}')
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

        return self.balance
    
    def name_tolower(self):
        self.name = self.name.lower()
        return self.name
    
    
customer1 = BankApp('Tunde', 105.44)
print(customer1.name_tolower())
print(customer1.deposit(1000))

# Inheritance in Python class
class Employee(): # super class

    def __init__(self,name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def bonus(self):
        bo = self.salary * 0.1
        return  self.salary + bo
    
class supervisor(Employee): # sub class

    def __init__(self, name, salary, designation, branch):
        self.branch = branch
        super().__init__(name, salary, designation)
    @property
    def bonus(self):
        return self.salary + (self.salary * 0.17)
    
    def report(self):
        return f"Hi {self.name}. You take home salary is {self.bonus}"

a = Employee('Tosin', 100, "Q/A")
print(a.bonus())

b = supervisor("Tunde", 10000, "Supervisor", "Yaba")
print(b.bonus)


