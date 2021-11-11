def median(arr):
    arr.sort()
    if(len(arr) % 2 == 0):
        index = len(arr)//2
        return (arr[index] + arr[index-1])/2
    else:
        index = len(arr)//2
        return arr[index]

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))