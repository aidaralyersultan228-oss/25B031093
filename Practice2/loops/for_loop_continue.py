# 1) skip even
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

# 2) skip a letter
for ch in "banana":
    if ch == "a":
        continue
    print(ch)

# 3) skip negatives
for x in [2, -1, 3, -5, 4]:
    if x < 0:
        continue
    print(x)

# 4) skip short words
words = ["hi", "hello", "a", "python"]
for w in words:
    if len(w) < 2:
        continue
    print(w)

# 5) skip specific value
for x in [1, 2, 3, 2, 4]:
    if x == 2:
        continue
    print(x)
