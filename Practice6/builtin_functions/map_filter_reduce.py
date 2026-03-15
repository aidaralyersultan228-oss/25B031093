from functools import reduce

# example list
numbers = [1, 2, 3, 4, 5, 6]

# map() → square each number
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter() → keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce() → sum all numbers
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)