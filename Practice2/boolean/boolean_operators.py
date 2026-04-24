# 1) and
print(True and False)

# 2) or
print(False or True)

# 3) not
print(not True)

# 4) combined
age = 18
has_id = True
print(age >= 18 and has_id)

# 5) operator precedence example
a, b, c = True, False, True
print(a or b and c)  # and happens before or
