# 1) Assign value
x = 5
print(x)

# 2) Change type
x = "Now I'm a string"
print(x)

# 3) Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

# 4) Unpack a list
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print(f1, f2, f3)

# 5) Global vs local example
x = "global"

def myfunc():
    x = "local"
    print("Inside function:", x)

myfunc()
print("Outside function:", x)