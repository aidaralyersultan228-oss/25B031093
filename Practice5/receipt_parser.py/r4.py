import re

a = input()

res = re.findall(r"[A-Z][a-z]+", a)

for i in res:
    print(i)