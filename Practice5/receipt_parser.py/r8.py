import re

a = input()

res = re.split(r'(?=[A-Z])', a)

for i in res:
    print(i)