# =========================================
# 1. OBJECT NIMA?
# =========================================

class Student:
    pass


student1 = Student()

# Student -> class
# student1 -> object


# =========================================
# 2. OBJECTGA ATTRIBUTE BERISH
# =========================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Mike", 24)

print(student1.name)
print(student1.age)


# student1 -> object
# name, age -> object attributes


# =========================================
# 3. BIR CLASSDAN BIR NECHTA OBJECT
# =========================================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("BMW", "M5")
car2 = Car("Mercedes", "AMG")

print(car1.brand, car1.model)
print(car2.brand, car2.model)


# car1 va car2 alohida objectlar


# =========================================
# 4. OBJECT ORQALI METHOD CHAQIRISH
# =========================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


person1 = Person("Mike")

person1.introduce()


# person1.introduce()
# object orqali method chaqirildi


# =========================================
# 5. OBJECT ATTRIBUTE O'ZGARTIRISH
# =========================================

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = User("Jon", 20)

print(user1.age)

user1.age = 21

print(user1.age)


# Natija:
# 20
# 21


# =========================================
# 6. OBJECT METHOD ORQALI O'ZGARISHI
# =========================================

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account1 = BankAccount(1000)

account1.deposit(500)

print(account1.balance)


# Natija:
# 1500


# =========================================
# 7. FINAL OBJECT EXAMPLE
# =========================================

class Product:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def show_info(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Amount:", self.amount)


iphone = Product(
    "iPhone",
    1000,
    5
)

iphone.show_info()
