import re

a = input()

res = re.search(r"a.*b", a)

print(res.group())