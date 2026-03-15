# enumerate() example
fruits = ["apple", "banana", "orange"]

for i, fruit in enumerate(fruits):
    print(i, fruit)


# zip() example
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)


# type checking
x = 10
print("Type of x:", type(x))
print("Is x int?", isinstance(x, int))


# type conversion
a = "25"
b = int(a)

print("Converted value:", b)
print("Type after conversion:", type(b))