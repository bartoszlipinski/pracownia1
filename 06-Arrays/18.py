arr1 = [76, 87, 42, 54, 25, 95, 72, 98]
arr2 = [8, 38, 99, 25, 72, 31, 56, 66]
arr3 = [46, 68, 74, 63, 66, 90, 17, 9]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)
print(arr1)
print(arr2)
print(arr3)
