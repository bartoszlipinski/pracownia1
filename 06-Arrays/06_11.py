arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]

def compare(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

print(compare(arr1,arr2))
        