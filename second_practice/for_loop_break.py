# 1)
for i in range(10):
    if i == 5:
        break
    print(i)

# 2) stop when found
for x in [3, 7, 9]:
    if x == 7:
        print("found")
        break

# 3) break on first even
for x in [1, 3, 4, 7]:
    if x % 2 == 0:
        print("first even:", x)
        break

# 4) break in string search
s = "hello world"
for ch in s:
    if ch == " ":
        break
    print(ch)

# 5) break nested (example)
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
