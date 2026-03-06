import re

with open("raw.txt", "r", encoding="utf-8") as f:
    x = f.read()

price_pattern = r"\d[\d ]*,\d{2}"

prices = re.findall(price_pattern, x)

for i in prices:
    print(i)