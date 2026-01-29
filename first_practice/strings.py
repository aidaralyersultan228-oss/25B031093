# Strings examples (up to 5)

# 1) String literals
print("Hello")
print('Hello')

# 2) Multiline string
text = """This is line 1
This is line 2"""
print(text)

# 3) Indexing and slicing
s = "Python"
print(s[0])     # P
print(s[0:3])   # Pyt

# 4) Useful methods
msg = "  hello world  "
print(msg.upper())
print(msg.strip())
print(msg.replace("world", "Python"))

# 5) f-strings
name = "Alice"
age = 18
print(f"{name} is {age} years old")