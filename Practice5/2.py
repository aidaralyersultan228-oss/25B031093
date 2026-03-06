import re

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

pattern = r"\d+\.\n(.+)"

product = re.findall(pattern, x)

for i in product:
    print(i)