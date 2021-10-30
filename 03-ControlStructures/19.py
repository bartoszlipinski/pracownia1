humanYears = int(input('Enter the dog\'s age in human years: '))

i = 0
dogYears = 0

while i < humanYears:
    if i < 2:
        dogYears += 10.5
    else:
        dogYears += 4
    i += 1
print(f'The dog\'s age in dog\'s years is {int(dogYears)} years')
