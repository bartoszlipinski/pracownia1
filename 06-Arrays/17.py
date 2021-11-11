firstArray = [4, 36, 12, 28, 9, 44, 5]
secondArray = [5, 1, 36]

for i in firstArray:
    exists = False
    for j in secondArray:
        if i == j:
            exists = True
    if not exists:
        print(i)