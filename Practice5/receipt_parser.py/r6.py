import re

a = input()

res = re.sub(r"[,. ]", ":", a)

print(res)