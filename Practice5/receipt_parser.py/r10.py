import re

a = input()

temp = re.sub(r"(?=[A-Z])", "_", a)
res = re.sub(r"[A-Z]+", lambda x: x.group(0).lower(), temp)


print(res)