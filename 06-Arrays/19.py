array = [2, 3, 2, 5, 8, 1, 9, 8]
uniqueArray = []

print(array)
print('Unique numbers: ', end="")
for i in array:
    num = array.count(i)
    if num == 1:
        print(i, end=" ")