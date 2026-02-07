# 1)
i = 1
while i <= 3:
    print(i)
    i += 1

# 2) sum 1..5
i, s = 1, 0
while i <= 5:
    s += i
    i += 1
print(s)

# 3) countdown
n = 3
while n > 0:
    print(n)
    n -= 1

# 4) input loop (example structure)
# while True:
#     txt = input("Type 'q' to quit: ")
#     if txt == "q":
#         break

# 5) build a string
i = 0
result = ""
while i < 4:
    result += "*"
    i += 1
print(result)
