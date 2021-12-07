import re

message = "To be, or not to be, that is the question"
vowels = re.findall("a|e|i|o|u|y", message)
print(f'Number of vowels: {len(vowels)}')
