import re

with open('sample3.txt') as f:
    text = f.read()
    words = re.findall(r"(\w{6,})", text)
    for word in words:
        print(word)
