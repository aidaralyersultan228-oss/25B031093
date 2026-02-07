# 1) skip even numbers
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 2) skip negatives
nums = [2, -1, 4, -3, 5]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# 3) skip a value
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 4) skip empty strings
arr = ["hi", "", "ok", ""]
i = 0
while i < len(arr):
    if arr[i] == "":
        i += 1
        continue
    print(arr[i])
    i += 1

# 5) print only multiples of 3
i = 0
while i < 10:
    i += 1
    if i % 3 != 0:
        continue
    print(i)
