# Height
a = 4
# Width
b = 15

for i in range(a):
    if i == 0 or i == a - 1:
        print(b*"*")
    else:
        print(f"*{(b-2)*' '}*")