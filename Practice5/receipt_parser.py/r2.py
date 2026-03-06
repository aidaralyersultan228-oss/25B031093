import re

a = "abb abb baabb"

pattern = r"ab{2,3}"

res = re.search(pattern, a)

if res:
    print(res.group())