# 1 default argument
def greet(name="Guest"):
    print("Hello", name)

# 2 keyword argument
def info(name, age):
    print(name, age)

# 3 positional argument
def multiply(a, b):
    print(a * b)

# 4 mixed arguments
def power(base, exp=2):
    print(base ** exp)

# 5 multiple parameters
def student(name, group, gpa):
    print(name, group, gpa)
    