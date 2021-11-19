array = [4,2,8,4,7,9,5]

def minmax(arr):
    arr.sort()
    newArray = [arr[0], arr[len(arr)-1]]
    return newArray

print(minmax(array))
