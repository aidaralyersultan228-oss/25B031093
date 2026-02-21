# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa


# 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year


# 3
class Animal:
    def __init__(self, age):
        self.age = age

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        self.breed = breed


# 4
class Employee:
    def __init__(self, salary):
        self.salary = salary

class Developer(Employee):
    def __init__(self, salary, projects):
        super().__init__(salary)
        self.projects = projects


# 5
class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width):
        super().__init__(color)
        self.width = width