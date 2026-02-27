# 1 simple generator (1 to n)
def count_up(n):
    for i in range(1, n+1):
        yield i


# 2 reverse generator
def reverse(n):
    for i in range(n, 0, -1):
        yield i


# 3 generator of squares
def squares(n):
    for i in range(n):
        yield i * i


# 4 even numbers generator
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# 5 fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b