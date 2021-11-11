array = [27,79,51,71,23,9,86,78,54,60]

evenNums = []
oddNums = []

for i in array:
    if i % 2 == 0:
        evenNums.append(i)
    else:
        oddNums.append(i)
array = evenNums
array.extend(oddNums)
print(array)