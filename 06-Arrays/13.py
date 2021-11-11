array = [8, 2, 5, 1, 9]


def to2ndPower(array):
    arr = []
    for i in array:
        arr.append(i ** 2)
    return arr


print('Array: ', end="")
for i in array:
    print(i, end=" ")

print("\n2nd Power: ", end="")
for i in to2ndPower(array):
    print(i, end=" ")
