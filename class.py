# =========================================
# 1. ODDIY CLASS
# =========================================

class Person:
    pass


person1 = Person()


# =========================================
# 2. __init__ VA self
# =========================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Mike", 24)

print(student1.name)
print(student1.age)


# self -> objectning o'zi
# name, age -> attribute


# =========================================
# 3. METHOD
# =========================================

class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student1 = Student("Mike")

student1.introduce()


# Class ichidagi function -> method


# =========================================
# 4. METHOD BILAN QIYMAT O'ZGARTIRISH
# =========================================

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(1000)

account.deposit(500)

print(account.balance)


# Natija:
# 1500


# =========================================
# 5. DEFAULT VALUE
# =========================================

class User:

    def __init__(self, name, country="Uzbekistan"):
        self.name = name
        self.country = country


user1 = User("Mike")

print(user1.name)
print(user1.country)


# =========================================
# 6. CLASS VARIABLE
# =========================================

class Student:

    school = "Python Academy"

    def __init__(self, name):
        self.name = name


student1 = Student("MIke")

print(student1.school)
print(student1.name)


# school -> class variable
# name -> instance variable


# =========================================
# 7. INHERITANCE
# =========================================

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Woof")


dog = Dog()

dog.eat()
dog.bark()


# Dog -> child class
# Animal -> parent class


# =========================================
# 8. PRIVATE ATTRIBUTE
# =========================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

print(account.get_balance())


# __balance -> private attribute


# =========================================
# 9. FINAL EXAMPLE
# =========================================

class Product:

    store = "Python Store"

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def sell(self, amount):

        if amount <= self.amount:
            self.amount -= amount
            print("Product sold")

        else:
            print("Not enough product")

    def show_info(self):

        print("Store:", self.store)
        print("Product:", self.name)
        print("Price:", self.price)
        print("Amount:", self.amount)


iphone = Product(
    "iPhone",
    1000,
    5
)

iphone.show_info()

iphone.sell(2)

iphone.show_info()
