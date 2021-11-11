array = [20.11,14.63,18.82,55.5,63.98,49.71,15.33,85.61,72.02,85.58]
num = float(input('Enter a real number: '))

greater = 0
for i in array:
    if i > num:
        greater += 1

print(f'Amount of numbers greater than {num}: {greater}')