from random import randint

array = [27, 79, 51, 71, 23, 9, 86, 78, 54, 60]


def rand_elem(arr):
    return array[randint(0, len(array) - 1)]


print(rand_elem(array))
