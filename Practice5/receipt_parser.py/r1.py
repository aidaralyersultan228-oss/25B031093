import re

a = "abb abb baabb"

pattern = r"ab*"

res = re.search(pattern, a)

if res:
    print(res.group())