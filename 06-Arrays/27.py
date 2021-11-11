array = [5, 4, 3, 2, 6, 5]


def tostring(arr):
    string = list(map(str, array))
    return ','.join(string)


print(tostring(array))
