import re 

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

pattern = r"Время:[\d.: ]*"

time = re.findall(pattern, x)

for i in time:
    print(i)