import re
a = input()

res = re.findall(r"[a-z]+_[a-z]+", a)

for i in res:
    print(i)

