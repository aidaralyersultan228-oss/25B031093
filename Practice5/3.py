import re

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

cnt = 0

price_pattern = r"Стоимость\n\d[\d ]*,\d{2}"

prices = re.findall(price_pattern, x)

for i in prices:
    i = i.replace(" ", "")
    i = i.replace(",", ".").replace("Стоимость", "")
    cnt += float(i)

print(cnt)