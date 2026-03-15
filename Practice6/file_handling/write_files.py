#3 Append new lines and verify content
with open("text.txt", "a") as f:
    f.write("\nnew line")

with open("text.txt", "r") as f:
    print(f.read())