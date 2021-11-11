names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longestName = ""

print("Names: ", end="")
for i in names:
    print(i, end=" ")
    if len(i) > len(longestName):
        longestName = i

print(f'\nLongest name: {longestName}')