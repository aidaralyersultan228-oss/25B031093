import re

a = input()

res = re.sub(r"(?=[A-Z])", " ", a)

print(res)