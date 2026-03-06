import re

a = input()

res = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), a)

print(res)