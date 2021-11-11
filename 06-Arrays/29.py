firstArray = [27, 79, 51, 71]
secondArray = [27, 79, 51, 71, 23, 9, 86, 78, 54, 60]

s = set()

for i in secondArray:
    s.add(i)

for j in firstArray:
    s.add(j)

if len(s) == len(secondArray):
    print('First is a subset of second')
else:
    print('First is not a subset of second')