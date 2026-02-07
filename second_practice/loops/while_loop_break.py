# 1)
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

# 2) stop when found
nums = [3, 5, 7, 9]
i = 0
while i < len(nums):
    if nums[i] == 7:
        print("Found 7")
        break
    i += 1

# 3) break on condition
x = 0
while x < 10:
    x += 1
    if x == 5:
        break
print("stopped at", x)

# 4) infinite loop with break
while True:
    word = "ok"
    print(word)
    break

# 5) break when too big
s = 0
i = 1
while True:
    s += i
    if s > 10:
        break
    i += 1
print(s)
