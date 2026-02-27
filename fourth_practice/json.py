import json

# 1 convert dict to JSON string
data = {"name": "John", "age": 30}
json_text = json.dumps(data)
print("JSON string:", json_text)


# 2 convert JSON string to dict
text = '{"city": "Almaty", "temp": 25}'
python_data = json.loads(text)
print("City:", python_data["city"])


# 3 nested JSON structure
nested = {
    "user": {
        "name": "Ali",
        "age": 20
    },
    "courses": ["Math", "Python"]
}

nested_json = json.dumps(nested, indent=4)
print("Nested JSON:\n", nested_json)


# 4 JSON array (list of objects)
students = [
    {"name": "Sara", "grade": 90},
    {"name": "Tim", "grade": 85}
]

students_json = json.dumps(students, indent=4)
print("Students JSON:\n", students_json)


# 5 sort JSON keys alphabetically
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print("Sorted keys JSON:\n", sorted_json)