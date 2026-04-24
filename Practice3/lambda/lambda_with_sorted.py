# 1 sort numbers descending
nums = [5, 2, 8, 1]
sorted_nums = sorted(nums, key=lambda x: x, reverse=True)

# 2 sort by length
words = ["apple", "kiwi", "banana"]
sorted_words = sorted(words, key=lambda x: len(x))

# 3 sort tuples by second element
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# 4 sort dictionary by value
d = {"a":3, "b":1, "c":2}
sorted_d = sorted(d.items(), key=lambda x: x[1])

# 5 sort students by age
students = [("Ali", 20), ("Sara", 18), ("Tim", 22)]
sorted_students = sorted(students, key=lambda x: x[1])