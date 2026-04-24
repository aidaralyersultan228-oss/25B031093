nums = [1, 2, 3, 4, 5, 6]

# 1
evens = list(filter(lambda x: x%2==0, nums))

# 2
odds = list(filter(lambda x: x%2!=0, nums))

# 3
greater_than_3 = list(filter(lambda x: x>3, nums))

# 4
small = list(filter(lambda x: x<4, nums))

# 5
positive = list(filter(lambda x: x>0, nums))