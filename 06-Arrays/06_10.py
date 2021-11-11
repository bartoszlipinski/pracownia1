array = [4, 3, 7, 1, 3]


def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum


def array2str(array):
    newStr = ""
    for i in array:
        newStr += f'{i} '
    return newStr


print(f'Array: {array2str(array)}\nSum of values: {sum(array)}')
