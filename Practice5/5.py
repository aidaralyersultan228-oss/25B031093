import re

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

pattern = r"Банковская карта"

result = re.findall(pattern, x)

for i in result:
    print(i)