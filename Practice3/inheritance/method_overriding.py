# 1
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")


# 2
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")


# 3
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def area(self):
        return 3.14


# 4
class Employee:
    def role(self):
        print("Employee")

class Manager(Employee):
    def role(self):
        print("Manager")


# 5
class Printer:
    def print_page(self):
        print("Black & White")

class ColorPrinter(Printer):
    def print_page(self):
        print("Color")