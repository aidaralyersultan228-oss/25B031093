import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()



product_pattern = r"(\d+\.)\s*\n([^\n]+)"
products = []

for number, name in re.findall(product_pattern, text):
    products.append(f"{number} {name.strip()}")


price_pattern = r"Стоимость\s*\n([\d ]+,\d{2})"
prices = re.findall(price_pattern, text)


total_pattern = r"ИТОГО:\s*\n([\d ]+,\d{2})"
total_match = re.search(total_pattern, text)
total = total_match.group(1) if total_match else None


payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group(1) if payment_match else None


datetime_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})"
datetime_match = re.search(datetime_pattern, text)

date = None
time = None
if datetime_match:
    date = datetime_match.group(1)
    time = datetime_match.group(2)


data = {
    "products": products,
    "prices": prices,
    "total": total,
    "payment_method": payment_method,
    "date": date,
    "time": time
}


print(json.dumps(data, indent=4, ensure_ascii=False))